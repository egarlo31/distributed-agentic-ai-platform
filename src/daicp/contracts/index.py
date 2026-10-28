"""Versioned local vector index with validation and atomic persistence."""
import json
import math
import os
import tempfile
from dataclasses import asdict, dataclass
from pathlib import Path
from .models import Evidence


@dataclass(frozen=True)
class KnowledgeIndex:
    """Portable index; normalized vectors keep cosine search deterministic."""

    model_name: str
    chunks: tuple[Evidence, ...]
    vectors: tuple[tuple[float, ...], ...]
    schema_version: int = 1

    def __post_init__(self) -> None:
        if self.schema_version != 1 or not self.model_name.strip():
            raise ValueError("Unsupported index version or missing model.")
        if not self.chunks or len(self.chunks) != len(self.vectors):
            raise ValueError("Index requires one vector per non-empty chunk.")
        if len({c.evidence_id for c in self.chunks}) != len(self.chunks):
            raise ValueError("Duplicate chunk IDs.")
        dimension = len(self.vectors[0])
        if not dimension:
            raise ValueError("Empty vectors are not supported.")
        for vector in self.vectors:
            if len(vector) != dimension:
                raise ValueError("Inconsistent vector dimensions.")
            self.normalize(vector)

    @staticmethod
    def normalize(vector) -> tuple[float, ...]:
        """Reject invalid/zero vectors instead of inventing a search score."""
        values = tuple(float(v) for v in vector)
        if not values or not all(math.isfinite(v) for v in values):
            raise ValueError("Embedding must contain finite values.")
        norm = math.sqrt(sum(v * v for v in values))
        if not math.isfinite(norm) or norm == 0:
            raise ValueError("Embedding norm must be finite and positive.")
        return tuple(v / norm for v in values)


class IndexRepository:
    """Read and atomically replace a single JSON index; never deserialize code."""

    def save(self, index: KnowledgeIndex, path: Path) -> None:
        path = Path(path)
        path.parent.mkdir(parents=True, exist_ok=True)
        payload = asdict(index)
        with tempfile.NamedTemporaryFile(mode="w", encoding="utf-8",
                                         dir=path.parent, delete=False) as stream:
            temporary = Path(stream.name)
            try:
                json.dump(payload, stream, ensure_ascii=False, allow_nan=False)
                stream.flush()
                os.fsync(stream.fileno())
            except BaseException:
                temporary.unlink(missing_ok=True)
                raise
        try:
            temporary.replace(path)
        finally:
            temporary.unlink(missing_ok=True)

    def load(self, path: Path) -> KnowledgeIndex:
        payload = json.loads(Path(path).read_text(encoding="utf-8"))
        return KnowledgeIndex(
            model_name=payload["model_name"],
            chunks=tuple(Evidence(**item) for item in payload["chunks"]),
            vectors=tuple(KnowledgeIndex.normalize(v) for v in payload["vectors"]),
            schema_version=payload["schema_version"],
        )
