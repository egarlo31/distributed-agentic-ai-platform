"""Behavioral integration tests for preparation -> index -> retrieval -> RCA.

Use unittest so the pipeline tests run without downloading ML runtimes/models.
The existing pytest validator suite remains separate.
"""
import csv
import io
import json
import tempfile
import unittest
from dataclasses import asdict
from datetime import datetime
from pathlib import Path
from unittest.mock import patch
from urllib.error import URLError

from daicp.contracts.incidents import IncidentRepository
from daicp.contracts.index import IndexRepository, KnowledgeIndex
from daicp.contracts.models import Evidence, Incident
from daicp.offline.data.preparation import DatasetPreparer, PreparedRecord
from daicp.offline.data.src001 import NetworkIncidentReader
from daicp.offline.data.coreops_preparation import CoreOpsIncidentReader, IncidentWindow
from daicp.offline.indexing.documents import ApprovedDocument, DocumentChunker
from daicp.offline.indexing.pipeline import KnowledgeIndexer
from daicp.backend.retrieval import RetrievalService
from daicp.backend.llm import LLMProvider, LLMProviderError, OllamaProvider
from daicp.backend.rca import RCAService, RCAOutputError
from daicp.backend.rca.output_schema import RCAOutputValidator
from daicp.backend.rca.prompt import RCAPromptBuilder


class FakeEmbeddings:
    """Small deterministic vectors make retrieval behavior inspectable."""

    model_name = "test-vectors-v1"

    def embed_query(self, text):
        return [1.0, 0.0] if "link" in text.lower() else [0.0, 1.0]

    def embed_documents(self, texts):
        return [self.embed_query(text) for text in texts]


class FakeLLM(LLMProvider):
    """Return cited JSON using only the first evidence actually received."""

    def __init__(self):
        self.calls = []

    def generate(self, prompt, system, schema):
        payload = json.loads(prompt)
        self.calls.append(payload)
        return json.dumps({"status": "hypotheses", "hypotheses": [{
            "explanation": "Investigate a possible connectivity problem.",
            "evidence_ids": [payload["evidence"][0]["evidence_id"]]}],
            "uncertainty": ["No causal conclusion has been verified."],
            "next_steps": ["Inspect connectivity counters."]})


class PipelineTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.root = Path(self.temporary.name)
        self.addCleanup(self.temporary.cleanup)
        self.embeddings = FakeEmbeddings()

    def index(self):
        link = self.root / "link.md"
        link.write_text("Link connectivity troubleshooting.")
        cpu = self.root / "cpu.md"
        cpu.write_text("CPU usage troubleshooting.")
        return KnowledgeIndexer(self.embeddings).build([
            ApprovedDocument(link, "TECH-LINK"), ApprovedDocument(cpu, "TECH-CPU")
        ], self.root / "index.json")

    def evidence(self):
        return Evidence("observed-1", "link timeout", "SRC-002", "logs/pcf.log", "line:1", "sha256")

    def test_index_roundtrip_retrieval_filter_and_abstention(self):
        index = self.index()
        loaded = IndexRepository().load(self.root / "index.json")
        self.assertEqual(index, loaded)
        retrieval = RetrievalService(loaded, self.embeddings)
        self.assertEqual(retrieval.search("link")[0].evidence.source_id, "TECH-LINK")
        self.assertEqual(retrieval.search("link", source_ids={"TECH-CPU"}), [])
        self.assertEqual(retrieval.search("link", source_ids=set()), [])

    def test_chunk_offsets_and_overlap_reproduce_source(self):
        path = self.root / "doc.txt"
        path.write_text("abcdefghijk")
        chunks = DocumentChunker(5, 2).read(ApprovedDocument(path, "TECH"))
        self.assertEqual([c.text for c in chunks], ["abcde", "defgh", "ghijk"])
        self.assertEqual(chunks[-1].locator, "characters:6:11")
        self.assertEqual(len({c.source_sha256 for c in chunks}), 1)

    def test_empty_approval_and_invalid_chunk_configuration(self):
        with self.assertRaises(ValueError):
            KnowledgeIndexer(self.embeddings).build([], self.root / "index.json")
        with self.assertRaises(ValueError):
            DocumentChunker(2, 2)

    def test_invalid_embedding_batch_does_not_replace_index(self):
        self.index()
        previous = (self.root / "index.json").read_bytes()
        self.embeddings.embed_documents = lambda texts: []
        with self.assertRaises(ValueError):
            KnowledgeIndexer(self.embeddings).build([
                ApprovedDocument(self.root / "link.md", "TECH")], self.root / "index.json")
        self.assertEqual(previous, (self.root / "index.json").read_bytes())

    def test_invalid_vectors_dimensions_and_model(self):
        for vectors in [((0, 0),), ((float("nan"), 1),), ((float("inf"), 1),)]:
            with self.subTest(vectors=vectors), self.assertRaises(ValueError):
                KnowledgeIndex("m", (self.evidence(),), vectors)
        index = self.index()
        self.embeddings.model_name = "other"
        with self.assertRaises(ValueError):
            RetrievalService(index, self.embeddings)
        self.embeddings.model_name = index.model_name
        self.embeddings.embed_query = lambda text: [1, 2, 3]
        with self.assertRaises(ValueError):
            RetrievalService(index, self.embeddings).search("link")

    def test_invalid_search_arguments(self):
        retrieval = RetrievalService(self.index(), self.embeddings)
        for kwargs in [{"query": " "}, {"query": "x", "top_k": 0},
                       {"query": "x", "min_score": float("nan")}]:
            with self.subTest(kwargs=kwargs), self.assertRaises(ValueError):
                retrieval.search(**kwargs)

    def test_src001_preparation_separates_labels_and_preserves_raw(self):
        path = self.root / "Network_Dataset.csv"
        fields = list(NetworkIncidentReader.OBSERVATION_FIELDS + NetworkIncidentReader.LABEL_FIELDS)
        with path.open("w", newline="") as stream:
            writer = csv.DictWriter(stream, fieldnames=fields)
            writer.writeheader()
            writer.writerows([{field: ("SECRET_LABEL" if field in NetworkIncidentReader.LABEL_FIELDS else "1")
                              for field in fields}] * 2)
        before = path.read_bytes()
        output = self.root / "prepared"
        manifest = DatasetPreparer().prepare(NetworkIncidentReader().read(path), output)
        self.assertEqual(sum(manifest["counts"].values()), 2)
        self.assertNotIn("SECRET_LABEL", (output / "incidents.jsonl").read_text())
        self.assertIn("SECRET_LABEL", (output / "references.jsonl").read_text())
        rows = [json.loads(line) for line in (output / "incidents.jsonl").read_text().splitlines()]
        self.assertEqual(rows[0]["partition"], rows[1]["partition"])
        incidents = list(IncidentRepository().read(output / "incidents.jsonl"))
        self.assertEqual(len(incidents), 2)
        self.assertEqual(path.read_bytes(), before)
        with self.assertRaises(ValueError):
            list(IncidentRepository().read(output / "references.jsonl"))
        with self.assertRaises(FileExistsError):
            DatasetPreparer().prepare([], output)

    def test_preparation_failure_is_transactional(self):
        item = PreparedRecord(Incident("i", "link", (self.evidence(),)), {}, "run1")
        output = self.root / "prepared"
        with self.assertRaises(ValueError):
            DatasetPreparer().prepare([item, item], output)
        self.assertFalse(output.exists())
        self.assertEqual(list(self.root.glob(".prepare-*")), [])
        with self.assertRaises(ValueError):
            DatasetPreparer().prepare([item], self.root / "raw" / "output")

    def test_groups_and_partition_endpoints(self):
        self.assertEqual(DatasetPreparer(0).partition("same-run"), "development")
        self.assertEqual(DatasetPreparer(1).partition("same-run"), "evaluation")
        self.assertEqual(DatasetPreparer().partition("same-run"), DatasetPreparer().partition("same-run"))

    def test_coreops_window_uses_logs_not_fault_targets(self):
        (self.root / "logs").mkdir()
        (self.root / "labels").mkdir()
        (self.root / "logs" / "pcf.log").write_text(
            "05/18 15:00:00.000: [app] INFO: outside\\n".replace("\\n", "\n") +
            "05/18 15:23:00.000: [sbi] ERROR: link failed\n" +
            "05/18 15:24:00.000: [sbi] ERROR: still failed\n")
        (self.root / "labels" / "fault_labels.json").write_text(json.dumps({"run_history": [{
            "fault_type": "SECRET_INJECTION", "targets": ["nrf"],
            "start_time": "2026-05-18T15:22:00+08:00", "end_time": "2026-05-18T15:30:00+08:00"}]}))
        window = IncidentWindow("neutral-1", datetime.fromisoformat("2026-05-18T15:22:00+08:00"),
                                datetime.fromisoformat("2026-05-18T15:30:00+08:00"), "run-1")
        record = next(CoreOpsIncidentReader("Asia/Shanghai", 1).read(self.root, [window]))
        self.assertEqual(len(record.incident.evidence), 1)
        encoded = json.dumps(asdict(record.incident))
        self.assertNotIn("SECRET_INJECTION", encoded)
        self.assertNotIn("outside", encoded)
        self.assertIn("Truncated", encoded)
        self.assertIn("SECRET_INJECTION", json.dumps(record.reference))

    def test_coreops_rejects_naive_window(self):
        with self.assertRaises(ValueError):
            IncidentWindow("i", datetime(2026, 1, 1), datetime(2026, 1, 2), "run1")

    def test_end_to_end_index_retrieval_provider_and_validated_rca(self):
        provider = FakeLLM()
        service = RCAService(RetrievalService(self.index(), self.embeddings), provider)
        result = service.analyze(Incident("incident-1", "link", (self.evidence(),)))
        self.assertEqual(result.status, "hypotheses")
        self.assertEqual(len(result.evidence), 2)
        self.assertEqual(result.hypotheses[0].evidence_ids, ("observed-1",))
        self.assertEqual(provider.calls[0]["incident_id"], "incident-1")

    def test_no_evidence_abstains_without_provider_call(self):
        provider = FakeLLM()
        retrieval = RetrievalService(self.index(), self.embeddings)
        with patch.object(retrieval, "search", return_value=[]):
            result = RCAService(retrieval, provider).analyze(Incident("i", "unknown"))
        self.assertEqual(result.status, "abstained")
        self.assertEqual(provider.calls, [])

    def test_rca_rejects_invented_citation_and_unknown_fields(self):
        payload = {"status": "hypotheses", "hypotheses": [{"explanation": "x", "evidence_ids": ["invented"]}],
                   "uncertainty": ["unknown"], "next_steps": []}
        validator = RCAOutputValidator()
        with self.assertRaises(RCAOutputError):
            validator.parse(json.dumps(payload), "i", (self.evidence(),))
        payload["hypotheses"][0]["evidence_ids"] = ["observed-1"]
        payload["secret"] = 1
        with self.assertRaises(RCAOutputError):
            validator.parse(json.dumps(payload), "i", (self.evidence(),))

    def test_rca_rejects_invalid_json_and_contradictory_status(self):
        for text in ["not json", "[]", json.dumps({"status": "hypotheses", "hypotheses": [],
                "uncertainty": ["unknown"], "next_steps": []})]:
            with self.subTest(text=text), self.assertRaises(RCAOutputError):
                RCAOutputValidator().parse(text, "i", ())

    def test_prompt_budget_fails_explicitly(self):
        with self.assertRaises(ValueError):
            RCAPromptBuilder(10).build(Incident("i", "link"), (self.evidence(),))

    def test_metrics_preserve_values_and_temporal_selection(self):
        from daicp.offline.data.coreops_metrics import CoreOpsMetricsReader
        metrics = self.root / "metrics" / "per_nf0525"
        metrics.mkdir(parents=True)
        (metrics / "pcf.csv").write_text(
            "timestamp;scrape_ok;restart_detected;private_column\n"
            "2026-05-18 15:00:00;1;0;outside\n"
            "2026-05-18 15:23:00;0;1;not_selected\n"
            "2026-05-18 15:24:00;1;0;not_selected\n")
        (self.root / "metrics/global_matrix.csv").write_text(
            "timestamp;data\n2026-05-18 15:23:00;pcf=DOWN;amf=UP\n")
        start = datetime.fromisoformat("2026-05-18T15:22:00+08:00")
        end = datetime.fromisoformat("2026-05-18T15:30:00+08:00")
        results = CoreOpsMetricsReader("Asia/Shanghai", max_rows_per_file=1).read(self.root, "i", start, end)
        self.assertEqual(len(results), 2)
        payload = json.loads(results[1].text)
        self.assertEqual(payload["omitted_matching_rows"], 1)
        self.assertEqual(payload["observations"][0]["scrape_ok"], "0")
        self.assertNotIn("private_column", results[1].text)
        self.assertIn("pcf=DOWN", results[0].text)

    def test_index_cannot_overwrite_source(self):
        path = self.root / "source.md"
        path.write_text("link documentation")
        with self.assertRaises(ValueError):
            KnowledgeIndexer(self.embeddings).build([ApprovedDocument(path, "TECH")], path)
        self.assertEqual(path.read_text(), "link documentation")

    def test_embedding_adapter_preserves_model_revision_and_query_document_routes(self):
        import sys
        from types import SimpleNamespace
        from unittest.mock import MagicMock
        transformer = MagicMock()
        transformer.encode_document.return_value = [[1, 0]]
        transformer.encode_query.return_value = [1, 0]
        constructor = MagicMock(return_value=transformer)
        with patch.dict(sys.modules, {"sentence_transformers": SimpleNamespace(SentenceTransformer=constructor)}):
            from daicp.embeddings import EmbeddingModel
            embedding = EmbeddingModel("qwen-local", revision="fixed-revision")
            self.assertEqual(embedding.model_name, "qwen-local@fixed-revision")
            embedding.embed_documents(["link"])
            embedding.embed_query("link")
            transformer.encode_document.assert_called_once_with(["link"], normalize_embeddings=True)
            transformer.encode_query.assert_called_once_with("link", normalize_embeddings=True)
            self.assertTrue(constructor.call_args.kwargs["local_files_only"])
            with self.assertRaises(ValueError):
                embedding.embed_documents([])
            with self.assertRaises(ValueError):
                embedding.embed_query(" ")

    def test_ollama_structured_request_and_transport_failures(self):
        provider = OllamaProvider(timeout=2)
        with patch("daicp.backend.llm.ollama_client.urlopen",
                   return_value=io.BytesIO(json.dumps({"response": "{}", "done": True}).encode())) as request:
            self.assertEqual(provider.generate("incident", "system", {"type": "object"}), "{}")
            payload = json.loads(request.call_args.args[0].data)
            self.assertFalse(payload["stream"])
            self.assertEqual(payload["format"], {"type": "object"})
            self.assertEqual(request.call_args.kwargs["timeout"], 2)
        with patch("daicp.backend.llm.ollama_client.urlopen", side_effect=URLError("offline")):
            with self.assertRaises(LLMProviderError):
                provider.generate("incident", "system", {})

    def test_ollama_rejects_truncated_or_empty_output(self):
        for body in [{"response": "{}", "done": False}, {"response": "", "done": True},
                     {"response": "{}", "done": True, "done_reason": "length"}, {"error": "missing"}]:
            with self.subTest(body=body), patch("daicp.backend.llm.ollama_client.urlopen",
                    return_value=io.BytesIO(json.dumps(body).encode())):
                with self.assertRaises(LLMProviderError):
                    OllamaProvider().generate("incident", "system", {})


if __name__ == "__main__":
    unittest.main()
