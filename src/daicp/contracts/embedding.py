"""Replaceable embedding contract, usable by indexing and retrieval."""
from typing import Protocol, Sequence


class EmbeddingProvider(Protocol):
    """Document and query vectors must use the same model and vector space."""

    model_name: str

    def embed_documents(self, texts: list[str]) -> Sequence[Sequence[float]]: ...

    def embed_query(self, query: str) -> Sequence[float]: ...
