# Root Cause Analysis and RAG Integration

- `service.py`: compose retrieval, incident evidence, provider generation, and validation.
- `prompt.py`: separate instructions from data, build context, and enforce its budget.
- `output_schema.py`: define hypotheses/results and validate JSON shape and citations.

`RCAService.analyze()` is the runtime RAG entry point: it retrieves relevant knowledge,
adds that evidence to the incident context, and generates a structured RCA response.
There is no separate `rag` package. Offline indexing supplies its knowledge artifact.
See [the RAG testing guide](../../../../docs/testing/rag.md) for a complete real-model
example and controlled integration tests.

## Integration

After preparing incidents and the index using the offline guides:

```python
from dataclasses import asdict
from pathlib import Path
from daicp.contracts.incidents import IncidentRepository
from daicp.contracts.index import IndexRepository
from daicp.embeddings import EmbeddingModel
from daicp.backend.retrieval import RetrievalService
from daicp.backend.llm import OllamaProvider
from daicp.backend.rca import RCAService

embeddings = EmbeddingModel(local_files_only=True)
index = IndexRepository().load(Path("data/processed/knowledge-v1/index.json"))
retrieval = RetrievalService(index, embeddings)
service = RCAService(retrieval, OllamaProvider(model="qwen3:8b"))
incident = next(IncidentRepository().read(
    Path("data/processed/src001-v1/incidents.jsonl"), partition="development"))
result = service.analyze(incident, top_k=5, min_score=0.25)
structured_result = asdict(result)
```

`query` optionally supplies a specific technical retrieval query. By default, the
summary and up to 2000 observation characters are used. All selected evidence is
returned with the answer to reconstruct its references. Obtain retrieval scores
through `retrieval.search`; scores are not converted into confidence or source facts.

## Validation and Limits

Results contain incident ID, `status` (`hypotheses` or `abstained`), hypotheses with
evidence IDs, uncertainty, next steps, and traceable evidence. Unknown fields,
uncited hypotheses, unavailable citations, and contradictory statuses are rejected.
`RCAOutputError` reports invalid responses; they are not silently repaired or accepted.
Without operational evidence or retrieved knowledge, the service abstains before
calling the model. The model may also abstain.

Citation validation establishes membership, not causal support. Human review and
causal evaluation remain necessary. Retrieved content is treated as data, but prompt
instructions do not guarantee immunity to malicious source instructions. The service
does not execute tools or remediation.

The default budget is 24000 serialized context characters, not an exact token count.
Use `RCAPromptBuilder(max_context_chars=...)` to change it. Oversized context fails
explicitly; select fewer chunks/observations or a smaller window. Evaluation references
are never loaded into this workflow.

## Verification

From the repository root with Python 3.12 or later:

```bash
PYTHONPATH=src python -m unittest discover -s tests -p test_pipeline.py -v
python -m pytest tests
lint-imports --no-cache
```

Controlled tests verify integration, label separation, persistence, partitioning,
retrieval, abstention, citations, and provider errors without downloading models.
Real inference additionally requires semantic dependencies, model files, and Ollama.
