"""Prepare SRC-001 network CSV observations without exposing attack labels."""
import csv
import hashlib
import json
from pathlib import Path
from typing import Iterator
from daicp.contracts.models import Evidence, Incident
from .preparation import PreparedRecord, SourceFingerprint


class NetworkIncidentReader:
    """Streaming, whitelist-based CSV adapter.

    PCAP/TXT filenames encode attack scenarios, so they are not added to runtime
    context automatically. Cross-source joins need separately verified alignment.
    Dataset labels describe scenarios; they are not proven root causes.
    """

    OBSERVATION_FIELDS = (
        "src_ip", "src_port", "dst_ip", "dst_port", "proto", "service", "duration",
        "src_bytes", "dst_bytes", "conn_state", "missed_bytes", "history",
        "src_pkts", "src_ip_bytes", "dst_pkts", "dst_ip_bytes", "ip_proto",
        "http_trans_depth", "files_total_bytes", "is_GET_mthd", "http_status_error",
        "is_file_transfered",
    )
    LABEL_FIELDS = ("attack_category", "attack_type", "traffic_type")

    def read(self, path: Path, limit: int | None = None) -> Iterator[PreparedRecord]:
        """Read all rows unless an explicit development limit is supplied."""
        if limit is not None and limit < 1:
            raise ValueError("limit must be positive or None.")
        path = Path(path).resolve()
        if path.name != "Network_Dataset.csv":
            raise ValueError("Expected SRC-001 Network_Dataset.csv.")
        digest = SourceFingerprint.digest(path)
        with path.open(encoding="utf-8-sig", newline="") as stream:
            reader = csv.DictReader(stream)
            if not set(self.OBSERVATION_FIELDS + self.LABEL_FIELDS).issubset(reader.fieldnames or []):
                raise ValueError("SRC-001 CSV is missing required observation/label fields.")
            for row_number, row in enumerate(reader, 2):
                if limit is not None and row_number - 2 >= limit:
                    break
                if None in row or any(value is None for value in row.values()):
                    raise ValueError(f"Malformed CSV record at line {row_number}.")
                text = json.dumps({key: row[key] for key in self.OBSERVATION_FIELDS}, sort_keys=True)
                incident_id = hashlib.sha256(f"{digest}:{row_number}".encode()).hexdigest()
                evidence = Evidence(incident_id + ":network", text, "SRC-001",
                                    str(path), f"csv_line:{row_number}", digest)
                # Identical observations cannot cross the development/evaluation boundary.
                # A stronger scenario/session split can be supplied by another adapter.
                group = hashlib.sha256(text.encode()).hexdigest()
                yield PreparedRecord(
                    Incident(incident_id, "Analyze the supplied network observation.", (evidence,)),
                    {"labels": {key: row[key] for key in self.LABEL_FIELDS},
                     "original_uid": row.get("uid"),
                     "preparation": {"limit": limit, "observation_fields": self.OBSERVATION_FIELDS},
                     "limitation": "Scenario labels do not establish causal RCA ground truth."},
                    "SRC-001:" + group,
                )
