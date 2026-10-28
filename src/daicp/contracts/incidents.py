"""Runtime reader for prepared incidents; evaluation reference files are rejected."""
import json
from pathlib import Path
from typing import Iterator
from .models import Evidence, Incident


class IncidentRepository:
    """Read only the versioned incident payload and optional partition selection."""

    def read(self, path: Path, partition: str | None = None) -> Iterator[Incident]:
        if partition not in (None, "development", "evaluation"):
            raise ValueError("Unknown partition.")
        with Path(path).open(encoding="utf-8") as stream:
            for line in stream:
                payload = json.loads(line)
                if set(payload) != {"partition", "incident"}:
                    raise ValueError("Expected incident artifact; references are not runtime inputs.")
                if payload["partition"] not in ("development", "evaluation"):
                    raise ValueError("Unknown artifact partition.")
                data = payload["incident"]
                if not isinstance(data, dict) or set(data) != {"incident_id", "summary", "evidence"}:
                    raise ValueError("Unexpected incident fields.")
                evidence = tuple(Evidence(**item) for item in data["evidence"])
                incident = Incident(data["incident_id"], data["summary"], evidence)
                if partition is None or partition == payload["partition"]:
                    yield incident
