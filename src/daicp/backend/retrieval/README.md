# Retrieval

`RetrievalService` performs cosine search over an existing `KnowledgeIndex`. It does
not process datasets, read evaluation labels, or call the LLM. Results contain chunks,
original source references, and scores; a score is not diagnostic certainty.

```python
from pathlib import Path
from daicp.contracts.index import IndexRepository
from daicp.embeddings import EmbeddingModel
from daicp.backend.retrieval import RetrievalService

embeddings = EmbeddingModel(local_files_only=True)
index = IndexRepository().load(Path("data/processed/knowledge-v1/index.json"))
retrieval = RetrievalService(index, embeddings)
results = retrieval.search("NF registration timeout", top_k=5, min_score=0.25)
```

`source_ids={"TECH-001"}` restricts sources; an empty set returns no results. Calibrate
the configurable threshold against development examples. Returning zero chunks is
valid. Empty queries, incompatible models, and invalid vectors are rejected. Ties
are resolved by evidence ID. Exact search scans vectors in memory without an external
database. For the generation step, see [RCA](../rca/README.md).
