"""Sentence Transformers adapter for the shared embedding-provider contract."""
from __future__ import annotations
from typing import TYPE_CHECKING
from daicp.schemas.validation import Validation

if TYPE_CHECKING:
    import numpy as np

model = "Qwen/Qwen3-Embedding-0.6B"


class EmbeddingModel:
    """Encode normalized query/document vectors using one explicit model revision.

    Loading is deferred until construction. Downloads require local_files_only=False;
    the caller controls model installation and device placement.
    """

    def __init__(self, model_name: str = model, *, revision: str | None = None,
                 local_files_only: bool = True, device: str | None = None) -> None:
        from sentence_transformers import SentenceTransformer

        if not model_name.strip():
            raise ValueError("An embedding model is required.")
        self.model_name = model_name if revision is None else f"{model_name}@{revision}"
        self.model = SentenceTransformer(model_name, revision=revision,
            local_files_only=local_files_only, device=device, trust_remote_code=False)

    def embed_documents(self, texts: list[str]) -> np.ndarray:
        """Encode document passages; reject an empty batch before inference."""
        Validation.validate_string_list(texts)
        if not texts or any(not text.strip() for text in texts):
            raise ValueError("Documents must contain non-empty text.")
        return self.model.encode_document(texts, normalize_embeddings=True)

    def embed_query(self, query: str) -> np.ndarray:
        """Encode one non-empty query in the same space as indexed documents."""
        Validation.validate_string_query(query)
        if not query.strip():
            raise ValueError("A non-empty query is required.")
        return self.model.encode_query(query, normalize_embeddings=True)
