# Testing Retrieval-Augmented Generation

## Implementation Map

RAG is the combination of retrieval, context augmentation, and generation. It is
implemented across existing classes rather than a separate `rag` package:

| Stage | Class | Module |
|---|---|---|
| Offline document ingestion and indexing | `KnowledgeIndexer` | `daicp.offline.indexing.pipeline` |
| Semantic encoding | `EmbeddingModel` | `daicp.embeddings.model` |
| Persist/load knowledge | `IndexRepository` | `daicp.contracts.index` |
| Retrieve relevant knowledge | `RetrievalService.search` | `daicp.backend.retrieval.service` |
| Coordinate runtime RAG for RCA | `RCAService.analyze` | `daicp.backend.rca.service` |
| Augment the model context | `RCAPromptBuilder.build` | `daicp.backend.rca.prompt` |
| Generate structured text | `OllamaProvider.generate` | `daicp.backend.llm.ollama_client` |
| Validate structure and citation IDs | `RCAOutputValidator.parse` | `daicp.backend.rca.output_schema` |

Runtime flow: incident → retrieval → incident plus retrieved evidence → LLM →
validated RCA hypotheses or abstention. Retrieval alone is only the retrieval stage;
`RCAService.analyze()` connects it to generation.

## 1. Controlled Tests Without Model Downloads

From the repository root, use Python 3.12 or later and an activated virtual environment:

```bash
python -m pip install -e '.[dev]'
python -m pytest tests -q
lint-imports --no-cache
```

To run only the complete controlled RAG integration test:

```bash
python -m pytest tests/test_pipeline.py::PipelineTests::test_end_to_end_index_retrieval_provider_and_validated_rca -v
```

This test builds a knowledge index, retrieves a matching chunk,
combines it with incident evidence, invokes a controlled LLM, and verifies the
structured answer and citation IDs. Other tests cover empty retrieval, abstention,
invalid citations, incompatible embeddings, context limits, evaluation-label
separation, source preservation, and Ollama request/error behavior.

The providers are deterministic test doubles. Passing these tests demonstrates
integration behavior, not the semantic quality of Qwen or the accuracy of diagnoses.
The repository's local `.venv` must have dependencies installed before these commands
will run; a virtual-environment directory alone is insufficient.

## 2. Real Local Inference

This is a manual integration check with an actual embedding model and Ollama.
Model downloads are explicit setup steps and may require substantial disk space.

### Prerequisites

1. Install the semantic adapter in the same activated environment:

   ```bash
   python -m pip install -e '.[dev,embeddings]'
   ```

2. Install Ollama separately if needed. Start it through the Ollama application or
   run `ollama serve` in a separate terminal if it is not already running.
3. Install the configured model and verify its presence:

   ```bash
   ollama pull qwen3:8b
   ollama list
   ```

4. Select an existing reviewed technical document in UTF-8 Markdown, text, or
   reStructuredText. Do not use `references.jsonl`, fault-injection labels, expected
   answers, or project planning documents as diagnostic knowledge.

### Build, Retrieve, and Generate

Run the following in Python from the repository root, after replacing the document
path with your actual approved document. The incident summary below is illustrative
manual input, not a dataset observation or evaluation result.

```python
from dataclasses import asdict
from pathlib import Path
from tempfile import TemporaryDirectory
import json

from daicp.offline.indexing import ApprovedDocument, KnowledgeIndexer
from daicp.contracts.index import IndexRepository
from daicp.contracts.models import Incident
from daicp.embeddings import EmbeddingModel
from daicp.backend.retrieval import RetrievalService
from daicp.backend.llm import OllamaProvider
from daicp.backend.rca import RCAService

approved_document = Path("/absolute/path/to/approved/connectivity.md")
# False explicitly permits the first model download. Use True once cached.
embeddings = EmbeddingModel(local_files_only=False)

with TemporaryDirectory(prefix="daicp-rag-check-") as workspace:
    index_path = Path(workspace) / "index.json"
    KnowledgeIndexer(embeddings).build(
        [ApprovedDocument(approved_document, "TECH-001")], index_path
    )
    index = IndexRepository().load(index_path)
    retrieval = RetrievalService(index, embeddings)
    query = "How should NF registration timeouts be investigated?"
    hits = retrieval.search(query, top_k=3, min_score=0.25)
    print("Retrieved chunks:")
    for hit in hits:
        print(hit.score, hit.evidence.evidence_id,
              hit.evidence.source_path, hit.evidence.locator)

    incident = Incident(
        incident_id="manual-rag-check-001",
        summary="An engineer reports repeated NF registration timeouts. "
                "Operational logs have not yet been provided.",
    )
    service = RCAService(retrieval, OllamaProvider(model="qwen3:8b"))
    result = service.analyze(incident, query=query, top_k=3, min_score=0.25)
    print(json.dumps(asdict(result), indent=2, ensure_ascii=False))
```

The temporary index is removed when the example exits. For a reusable index, choose
a path under `data/processed/` and follow the knowledge-indexing guide. To analyze
prepared operational evidence instead of manual input, replace the `Incident(...)`
construction with an incident from `IncidentRepository.read(...)`; see the RCA guide.

### What to Inspect

- Retrieval scores and chunk text should be relevant to the query. Scores are not
  probabilities or confidence values.
- Source paths, offsets, and hashes should identify the original technical material.
- Every generated hypothesis must cite IDs present in `result.evidence`.
- Missing observations should be acknowledged in `uncertainty`.
- `status="abstained"` is valid when evidence is insufficient. If retrieval returns
  no chunks and the incident has no evidence, the service skips the LLM entirely;
  that run has not tested actual generation.
- A valid JSON response and valid citation IDs do not establish a correct root cause.
  Assess factual support separately against independent evaluation references.

### Common Failures

| Symptom | Action |
|---|---|
| `ModuleNotFoundError` | Activate the intended environment and install the required extras. |
| Approved document does not exist | Replace the example path with an existing reviewed file. |
| Embedding model is unavailable locally | Explicitly permit its initial download or provide a cached local model. |
| No retrieved chunks | Inspect source coverage, chunk text, query, and development-calibrated threshold. |
| Embedding identity/dimension mismatch | Rebuild using the same model, revision, and configuration as retrieval. |
| `LLMProviderError` | Check Ollama, model availability, timeout, and generation limit. |
| Context exceeds its budget | Reduce chunk count, selected observations, or incident-window size. |
| `RCAOutputError` | Inspect the model output; invalid citations/structure are rejected, not silently repaired. |

Official provider documentation: [Ollama Generate](https://docs.ollama.com/api/generate).
