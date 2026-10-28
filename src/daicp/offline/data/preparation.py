"""Reusable preparation records, deterministic partitions and artifact writing."""
import hashlib
import json
import shutil
import tempfile
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Iterable
from daicp.contracts.models import Evidence, Incident


@dataclass(frozen=True)
class PreparedRecord:
    """Offline-only pairing; the reference is never serialized into the incident."""

    incident: Incident
    reference: dict
    group_id: str


class SourceFingerprint:
    """Hash large source files in bounded memory for exact provenance."""

    @staticmethod
    def digest(path: Path) -> str:
        digest = hashlib.sha256()
        with Path(path).open("rb") as stream:
            for block in iter(lambda: stream.read(1024 * 1024), b""):
                digest.update(block)
        return digest.hexdigest()


class DatasetPreparer:
    """Stream records into a new version directory with separated references.

    A group always belongs to one partition. No record-level random split is
    performed; callers must choose independent groups for their experiment.
    Existing versions and raw sources are never overwritten.
    """

    def __init__(self, evaluation_fraction: float = 0.2, seed: str = "daicp-v1") -> None:
        if not 0 <= evaluation_fraction <= 1:
            raise ValueError("evaluation_fraction must be within [0, 1].")
        self.evaluation_fraction, self.seed = evaluation_fraction, seed

    def partition(self, group_id: str) -> str:
        value = int(hashlib.sha256(f"{self.seed}:{group_id}".encode()).hexdigest(), 16)
        return "evaluation" if value / (1 << 256) < self.evaluation_fraction else "development"

    def prepare(self, records: Iterable[PreparedRecord], output: Path) -> dict:
        output = Path(output).resolve()
        if output.exists():
            raise FileExistsError("Choose a new output version; existing artifacts are immutable.")
        if "raw" in output.parts:
            raise ValueError("Prepared outputs must not be written under raw data.")
        output.parent.mkdir(parents=True, exist_ok=True)
        staging = Path(tempfile.mkdtemp(prefix=".prepare-", dir=output.parent))
        counts = {"development": 0, "evaluation": 0}
        seen = set()
        sources = {}
        try:
            with (staging / "incidents.jsonl").open("w", encoding="utf-8") as incidents, \
                 (staging / "references.jsonl").open("w", encoding="utf-8") as references:
                for record in records:
                    if record.incident.incident_id in seen:
                        raise ValueError("Duplicate incident ID; do not merge ambiguous records.")
                    if not record.group_id.strip():
                        raise ValueError("A non-empty partition group is required.")
                    seen.add(record.incident.incident_id)
                    partition = self.partition(record.group_id)
                    for evidence in record.incident.evidence:
                        previous = sources.setdefault(evidence.source_path, evidence.source_sha256)
                        if previous != evidence.source_sha256:
                            raise ValueError("Source changed within this preparation run.")
                    incidents.write(json.dumps({"partition": partition,
                        "incident": asdict(record.incident)}, ensure_ascii=False, allow_nan=False) + "\n")
                    references.write(json.dumps({"incident_id": record.incident.incident_id,
                        "partition": partition, "reference": record.reference},
                        ensure_ascii=False, allow_nan=False) + "\n")
                    counts[partition] += 1
            if not seen:
                raise ValueError("No incident records were prepared.")
            manifest = {"schema_version": 1, "seed": self.seed,
                        "evaluation_fraction": self.evaluation_fraction,
                        "counts": counts, "sources": sources,
                        "separation": "references.jsonl is evaluation-only"}
            (staging / "manifest.json").write_text(json.dumps(manifest, indent=2), encoding="utf-8")
            staging.rename(output)
            return manifest
        finally:
            if staging.exists():
                shutil.rmtree(staging)
