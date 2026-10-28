"""Explicitly approved text ingestion; no recursive dataset auto-discovery."""
from dataclasses import dataclass
from hashlib import sha256
from pathlib import Path
from daicp.contracts.models import Evidence


@dataclass(frozen=True)
class ApprovedDocument:
    """Caller approval is explicit; use only technical knowledge without labels."""

    path: Path
    source_id: str


class DocumentChunker:
    """Deterministic character windows with exact offsets and source hashes."""

    def __init__(self, chunk_size: int = 1200, overlap: int = 150) -> None:
        if chunk_size < 1 or not 0 <= overlap < chunk_size:
            raise ValueError("Require chunk_size > overlap >= 0.")
        self.chunk_size, self.overlap = chunk_size, overlap

    def read(self, document: ApprovedDocument) -> list[Evidence]:
        path = Path(document.path).resolve()
        if path.suffix.lower() not in {".txt", ".md", ".rst"}:
            raise ValueError("Only UTF-8 technical text (.txt, .md, .rst) is supported.")
        raw = path.read_bytes()
        text = raw.decode("utf-8")
        digest = sha256(raw).hexdigest()
        chunks = []
        for start in range(0, len(text), self.chunk_size - self.overlap):
            end = min(start + self.chunk_size, len(text))
            body = text[start:end]
            if body.strip():
                key = f"{document.source_id}:{path}:{digest}:{start}:{end}"
                chunks.append(Evidence(
                    sha256(key.encode()).hexdigest(), body, document.source_id,
                    str(path), f"characters:{start}:{end}", digest,
                ))
            if end == len(text):
                break
        return chunks
