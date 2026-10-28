# Approved Knowledge Indexing

- `documents.py`: `ApprovedDocument` expresses explicit selection; `DocumentChunker`
  produces chunks with character offsets and the original file SHA-256.
- `pipeline.py`: `KnowledgeIndexer` coordinates chunking, batched embeddings, and
  persistence through `IndexRepository`.
- `daicp.contracts.index`: version 1 JSON format and atomic storage shared with
  retrieval, without backend dependencies on offline processing.

```python
from pathlib import Path
from daicp.embeddings import EmbeddingModel
from daicp.offline.indexing import ApprovedDocument, KnowledgeIndexer

embeddings = EmbeddingModel(local_files_only=True)
KnowledgeIndexer(embeddings).build([
    ApprovedDocument(Path("knowledge/approved/connectivity.md"), "TECH-001"),
], Path("data/processed/knowledge-v1/index.json"))
```

The example document must exist and have been reviewed as technical knowledge.
No synthetic knowledge is supplied, and `docs/` or `data/` are not indexed automatically.
The caller must exclude labels, evaluation references, and expected answers;
`ApprovedDocument` expresses approval but does not assess content automatically.
Only UTF-8 `.md`, `.txt`, and `.rst` documents are supported. Other formats require
reviewed conversion before ingestion. Offsets refer to the original decoded text.

Install the semantic adapter with `python -m pip install -e '.[embeddings]'`.
The Qwen model must be available locally; `local_files_only=False` explicitly permits
downloading it. `revision` pins a model revision and becomes part of the index identity;
use exactly the same model, revision, and configuration for retrieval. The adapter
uses asymmetric `encode_document` and `encode_query` routes. It does not train models.

The index stores chunks, paths, identifiers, hashes, and normalized vectors. It rejects
empty sources, duplicate IDs, zero/non-finite vectors, and inconsistent dimensions.
A failed build leaves the previous index untouched. This local, exact, in-memory
implementation is intended for an MVP corpus, not massive collections or an external
vector database service.
