"""Coordinate approved document chunking and batched embedding generation."""
from pathlib import Path
from daicp.contracts.embedding import EmbeddingProvider
from daicp.contracts.index import IndexRepository, KnowledgeIndex
from .documents import ApprovedDocument, DocumentChunker


class KnowledgeIndexer:
    """Build an index only from the supplied approval list, never raw labels."""

    def __init__(self, embeddings: EmbeddingProvider,
                 chunker: DocumentChunker | None = None,
                 repository: IndexRepository | None = None,
                 batch_size: int = 32) -> None:
        if batch_size < 1:
            raise ValueError("batch_size must be positive.")
        self.embeddings = embeddings
        self.chunker = chunker or DocumentChunker()
        self.repository = repository or IndexRepository()
        self.batch_size = batch_size

    def build(self, documents: list[ApprovedDocument], output: Path) -> KnowledgeIndex:
        output = Path(output).resolve()
        if "raw" in output.parts or output in {Path(doc.path).resolve() for doc in documents}:
            raise ValueError("Index output must be separate from raw sources and approved documents.")
        chunks = [chunk for document in documents for chunk in self.chunker.read(document)]
        if not chunks:
            raise ValueError("No approved non-empty documents.")
        vectors = []
        for start in range(0, len(chunks), self.batch_size):
            batch = chunks[start:start + self.batch_size]
            encoded = self.embeddings.embed_documents([chunk.text for chunk in batch])
            if len(encoded) != len(batch):
                raise ValueError("Embedding provider returned an incorrect batch size.")
            vectors.extend(KnowledgeIndex.normalize(vector) for vector in encoded)
        index = KnowledgeIndex(self.embeddings.model_name, tuple(chunks), tuple(vectors))
        self.repository.save(index, output)
        return index
