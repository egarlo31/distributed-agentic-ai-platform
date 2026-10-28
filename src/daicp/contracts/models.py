"""Serializable evidence and incident contracts shared by producers and consumers."""
from dataclasses import dataclass, field


@dataclass(frozen=True)
class Evidence:
    """A source-derived observation or approved knowledge chunk, never ground truth."""

    evidence_id: str
    text: str
    source_id: str
    source_path: str
    locator: str
    source_sha256: str

    def __post_init__(self) -> None:
        for value in (self.evidence_id, self.text, self.source_id, self.source_path,
                      self.locator, self.source_sha256):
            if not isinstance(value, str) or not value.strip():
                raise ValueError("Evidence fields must be non-empty strings.")


@dataclass(frozen=True)
class Incident:
    """Runtime-safe input. Evaluation labels intentionally have no field here."""

    incident_id: str
    summary: str
    evidence: tuple[Evidence, ...] = field(default_factory=tuple)

    def __post_init__(self) -> None:
        if not self.incident_id.strip() or not self.summary.strip():
            raise ValueError("Incident ID and summary are required.")
        ids = [item.evidence_id for item in self.evidence]
        if len(ids) != len(set(ids)):
            raise ValueError("Incident evidence IDs must be unique.")
