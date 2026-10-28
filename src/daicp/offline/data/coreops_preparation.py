"""Prepare CoreOps windows using observed logs and separate ground truth."""
import hashlib
import json
import re
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Iterator
from zoneinfo import ZoneInfo
from daicp.contracts.models import Evidence, Incident
from .preparation import PreparedRecord, SourceFingerprint
from .coreops_metrics import CoreOpsMetricsReader


@dataclass(frozen=True)
class IncidentWindow:
    """Externally selected window; ID/group must not describe the injected fault.

    The year and timezone must be explicit because Open5GS timestamps omit them.
    Selection by ground truth is an offline experimental decision and must be
    reported in the evaluation protocol, not interpreted as online detection.
    """

    incident_id: str
    start: datetime
    end: datetime
    group_id: str

    def __post_init__(self) -> None:
        if not self.incident_id.strip() or not self.group_id.strip():
            raise ValueError("Neutral incident ID and experimental group are required.")
        if self.start.utcoffset() is None or self.end.utcoffset() is None:
            raise ValueError("Window timestamps must include timezone information.")
        if self.end < self.start:
            raise ValueError("Window end precedes start.")


class CoreOpsIncidentReader:
    """Stream exact log observations per window; exclude injection records.

    All available NF logs are considered, rather than selecting NFs from fault
    targets. No causal conclusion is inferred from overlapping fault labels.
    """

    TIMESTAMP = re.compile(r"^(\d{2}/\d{2} \d{2}:\d{2}:\d{2}\.\d+):")

    def __init__(self, log_timezone: str, max_lines_per_file: int = 30,
                 metrics_columns: tuple[str, ...] = ("scrape_ok", "restart_detected"),
                 max_metric_rows: int = 5) -> None:
        if max_lines_per_file < 1:
            raise ValueError("max_lines_per_file must be positive.")
        self.timezone = ZoneInfo(log_timezone)
        self.max_lines_per_file = max_lines_per_file
        self.metrics = CoreOpsMetricsReader(log_timezone, metrics_columns, max_metric_rows)

    def read(self, root: Path, windows: list[IncidentWindow]) -> Iterator[PreparedRecord]:
        root = Path(root).resolve()
        paths = sorted((root / "logs").glob("*.log"))
        if not paths:
            raise ValueError("No CoreOps operational logs found.")
        labels_path = root / "labels/fault_labels.json"
        labels = json.loads(labels_path.read_text(encoding="utf-8"))["run_history"]
        hashes = {path: SourceFingerprint.digest(path) for path in paths}
        for window in windows:
            local_start, local_end = window.start.astimezone(self.timezone), window.end.astimezone(self.timezone)
            if local_start.year != local_end.year:
                raise ValueError("Split year-crossing windows explicitly; logs omit the year.")
            evidence = []
            for path in paths:
                selected = []
                matching = 0
                with path.open(encoding="utf-8", errors="strict") as stream:
                    for number, line in enumerate(stream, 1):
                        match = self.TIMESTAMP.match(line)
                        if not match:
                            continue
                        timestamp = datetime.strptime(
                            f"{local_start.year}/{match.group(1)}", "%Y/%m/%d %H:%M:%S.%f"
                        ).replace(tzinfo=self.timezone)
                        if local_start <= timestamp <= local_end:
                            matching += 1
                            if len(selected) < self.max_lines_per_file:
                                selected.append((number, line.rstrip()))
                if selected:
                    text = "\n".join(f"{number}: {line}" for number, line in selected)
                    if matching > len(selected):
                        text += f"\n[Truncated: {matching - len(selected)} additional matching lines omitted.]"
                    key = hashlib.sha256(f"{window.incident_id}:{path}:{hashes[path]}".encode()).hexdigest()
                    evidence.append(Evidence(key, text, "SRC-002", str(path),
                        f"lines:{selected[0][0]}:{selected[-1][0]};window:{window.start.isoformat()}/{window.end.isoformat()}",
                        hashes[path]))
            evidence.extend(self.metrics.read(root, window.incident_id, window.start, window.end))
            if not evidence:
                raise ValueError(f"No operational evidence in window {window.incident_id}; inspect coverage.")
            overlapping = [label for label in labels
                if datetime.fromisoformat(label["start_time"]) <= window.end
                and datetime.fromisoformat(label["end_time"]) >= window.start]
            yield PreparedRecord(
                Incident(window.incident_id, f"Investigate network behavior from {window.start.isoformat()} "
                         f"to {window.end.isoformat()}.", tuple(evidence)),
                {"overlapping_faults": overlapping,
                 "labels_path": str(labels_path),
                 "labels_sha256": SourceFingerprint.digest(labels_path),
                 "log_timezone": str(self.timezone),
                 "preparation": {"max_lines_per_file": self.max_lines_per_file,
                    "metric_columns": self.metrics.columns,
                    "max_metric_rows": self.metrics.max_rows_per_file},
                 "limitation": "Injected faults may overlap and need not have observable effects."},
                window.group_id,
            )
