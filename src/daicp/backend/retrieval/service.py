"""Local cosine retrieval with provenance, filtering and explicit abstention."""
from dataclasses import dataclass
from daicp.contracts.embedding import EmbeddingProvider
from daicp.contracts.index import KnowledgeIndex
from daicp.contracts.models import Evidence


@dataclass(frozen=True)
class RetrievedEvidence:
    """Knowledge chunk and its cosine score (not a probability of correctness)."""

    evidence: Evidence
    score: float


class RetrievalService:
    """Read-only search; a threshold may legitimately return zero results."""

    def __init__(self, index: KnowledgeIndex, embeddings: EmbeddingProvider) -> None:
        if index.model_name != embeddings.model_name:
            raise ValueError("Query embedding model differs from the indexed model.")
        self.index, self.embeddings = index, embeddings

    def search(self, query: str, top_k: int = 5, min_score: float = 0.25,
               source_ids: set[str] | None = None) -> list[RetrievedEvidence]:
        if not isinstance(query, str) or not query.strip():
            raise ValueError("Query must be non-empty text.")
        if isinstance(top_k, bool) or not isinstance(top_k, int) or top_k < 1:
            raise ValueError("top_k must be a positive integer.")
        if not -1 <= min_score <= 1:
            raise ValueError("min_score must be within [-1, 1].")
        query_vector = KnowledgeIndex.normalize(self.embeddings.embed_query(query))
        if len(query_vector) != len(self.index.vectors[0]):
            raise ValueError("Query embedding dimension differs from the index.")
        results = []
        for chunk, vector in zip(self.index.chunks, self.index.vectors, strict=True):
            if source_ids is not None and chunk.source_id not in source_ids:
                continue
            normalized = KnowledgeIndex.normalize(vector)
            score = max(-1.0, min(1.0, sum(a * b for a, b in zip(query_vector, normalized))))
            if score >= min_score:
                results.append(RetrievedEvidence(chunk, score))
        return sorted(results, key=lambda item: (-item.score, item.evidence.evidence_id))[:top_k]
