"""Windowed CoreOps metrics observations with explicit temporal assumptions."""
import csv
import hashlib
import json
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo
from daicp.contracts.models import Evidence
from .preparation import SourceFingerprint


class CoreOpsMetricsReader:
    """Select metric rows without reading aligned fault windows or injection labels.

    Global availability uses the source's variable-width semicolon format.
    Per-NF metrics use an explicit column allowlist to bound model context.
    """

    def __init__(self, timezone: str, columns: tuple[str, ...] = ("scrape_ok", "restart_detected"),
                 max_rows_per_file: int = 5) -> None:
        if max_rows_per_file < 1 or not columns or len(set(columns)) != len(columns):
            raise ValueError("Unique metric columns and a positive row limit are required.")
        self.timezone = ZoneInfo(timezone)
        self.columns, self.max_rows_per_file = columns, max_rows_per_file
        self._hashes: dict[Path, str] = {}

    def _time(self, value: str) -> datetime:
        parsed = datetime.fromisoformat(value)
        return parsed.replace(tzinfo=self.timezone) if parsed.utcoffset() is None else parsed

    def read(self, root: Path, incident_id: str, start: datetime, end: datetime) -> list[Evidence]:
        """Keep exact observed values and disclose any omitted matching rows."""
        root = Path(root)
        paths = sorted((root / "metrics/per_nf0525").glob("*.csv"))
        global_path = root / "metrics/global_matrix.csv"
        if global_path.exists():
            paths.insert(0, global_path)
        evidence = []
        for path in paths:
            selected = []
            count = 0
            with path.open(encoding="utf-8-sig", newline="") as stream:
                reader = csv.reader(stream, delimiter=";")
                header = next(reader, [])
                if not header or header[0] != "timestamp":
                    raise ValueError(f"Missing timestamp column in {path}.")
                global_format = path == global_path
                if not global_format and not set(self.columns).issubset(header):
                    raise ValueError(f"Missing configured metric columns in {path}.")
                for number, row in enumerate(reader, 2):
                    if not row:
                        continue
                    if start <= self._time(row[0]) <= end:
                        count += 1
                        if len(selected) < self.max_rows_per_file:
                            if global_format:
                                # Preserve statuses as observations, not labels.
                                values = {"timestamp": row[0], "availability": row[1:]}
                            else:
                                if len(row) != len(header):
                                    raise ValueError(f"Malformed metric row {number} in {path}.")
                                mapping = dict(zip(header, row, strict=True))
                                values = {key: mapping[key] for key in ("timestamp", *self.columns)}
                            selected.append((number, values))
            if selected:
                if path not in self._hashes:
                    self._hashes[path] = SourceFingerprint.digest(path)
                digest = self._hashes[path]
                key = hashlib.sha256(f"{incident_id}:{path}:{digest}:metrics".encode()).hexdigest()
                text = json.dumps({"observations": [values for _, values in selected],
                                   "omitted_matching_rows": count - len(selected)}, sort_keys=True)
                evidence.append(Evidence(key, text, "SRC-002", str(path),
                    f"csv_lines:{','.join(str(n) for n, _ in selected)};window:{start.isoformat()}/{end.isoformat()}",
                    digest))
        return evidence
