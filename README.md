# DAICP — Data, Retrieval, and Diagnosis Components

Python project supporting troubleshooting and root cause analysis in 5G networks.
The MVP architecture and scope are described in `docs/`.

The repository provides offline preparation of SRC-001/SRC-002, approved knowledge
indexing, local semantic retrieval, structured RCA, and an Ollama provider. These
components integrate through classes and shared contracts. An application interface,
agent, and tool execution are outside the implemented component scope.

## Installation

Use Python 3.12 or later in a virtual environment, from the repository root:

```bash
python -m pip install -r requirements.txt
python -m pip install -e '.[embeddings]'
```

Semantic models and Ollama must be prepared separately. Importing modules does not
download models. Existing PCAP audits require external `capinfos` and `tshark` tools.
Files under `data/raw/` are original sources and must remain unchanged.

## Components and Guides

| Component | Responsibility | Guide |
|---|---|---|
| Offline / data | Audits, incidents, and separate evaluation references | [Data preparation](src/daicp/offline/data/README.md) |
| Offline / knowledge | Chunk and embed approved documents | [Knowledge indexing](src/daicp/offline/indexing/README.md) |
| Retrieval | Search chunks while preserving provenance | [Retrieval](src/daicp/backend/retrieval/README.md) |
| RCA / RAG integration | Augment incident context and generate validated hypotheses | [RCA](src/daicp/backend/rca/README.md) |
| LLM | Abstract inference and implement Ollama | [LLM provider](src/daicp/backend/llm/README.md) |
| Contracts | Incidents, evidence, embeddings, and persistent indexes | `src/daicp/contracts/` |

## Where RAG Lives

Retrieval-Augmented Generation is a workflow across these components, rather than
a separate `rag` package. `RCAService.analyze()` retrieves knowledge through
`RetrievalService`, augments the incident context through `RCAPromptBuilder`, and
calls `LLMProvider.generate()`. `RCAOutputValidator` validates the resulting JSON and
citation IDs. `KnowledgeIndexer` prepares the knowledge index offline.

[Testing RAG: controlled integration and real local inference](docs/testing/rag.md)
provides executable examples, prerequisites, and expected results.

Evaluation references remain separate from retrieval and RCA. Available documents
and datasets are not automatically approved knowledge: the responsible user must
select technical documents for indexing and exclude evaluation answers.

## Tests

```bash
python -m pytest tests
lint-imports --no-cache
```

`tests/test_pipeline.py` uses controlled providers to verify the workflow without
real models, including label leakage, persistence, abstention, and citations.
`tests/test_validators.py` retains input-validation tests. The architecture contract
prevents backend imports of offline processing. Generated hypotheses require review:
a valid citation does not prove causality.

## Project Language

Project-authored code, comments, docstrings, documentation, test descriptions, and
configuration labels use English. Preserve proper names and original source data,
including third-party logs, labels, metadata, and quoted source material.
