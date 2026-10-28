"""Dataset-specific audit utilities; evaluation labels remain offline."""
import json
import shutil
from pathlib import Path

import pandas as pd
import re
from collections import Counter, defaultdict
from datetime import datetime, timedelta, timezone

from .profiling import Quality


class PacketTools:
    """Locate external packet-audit executables without running them."""

    def __init__(self, *names: str) -> None:
        self.names = names

    def get_packet_tools(self) -> dict[str, str]:
        """Locate required packet analysis tools."""
        tools = {name: shutil.which(name) for name in self.names}
        missing = [name for name, path in tools.items() if path is None]

        if missing:
            raise RuntimeError(f"Missing PCAP tools: {missing}")

        return tools

class CoreOps:
    """Inspect CoreOps quality, temporal consistency, logs and metric coverage."""


    @staticmethod
    def audit_coreops_quality(root: Path) -> dict[str, pd.DataFrame]:
        """Run quality checks on the selected CoreOps dataset."""

        with (root / "labels/fault_labels.json").open(encoding="utf-8") as f:
            faults = pd.json_normalize(json.load(f)["run_history"])

        windows = pd.read_json(root / "metrics/aligned_fault_window.json")

        results = [
            Quality.profile_dataframe(faults, "Fault Labels", "fault_id"),
            Quality.profile_dataframe(windows, "Fault Windows", "fault_id")
        ]

        for path in sorted((root / "metrics/per_nf0525").glob("*.csv")):
            df = pd.read_csv(path, sep=";", low_memory=False)
            results.append(Quality.profile_dataframe(df, path.stem))
            del df

        missing = (
            faults.isna().mean().mul(100)
            .loc[lambda x: x > 0]
            .sort_values(ascending=False)
            .rename_axis("column")
            .reset_index(name="missing_pct")
        )

        return {
            "summary": pd.DataFrame(results),
            "validations": Quality.validate_faults(faults),
            "missing_fields": missing
        }

    @staticmethod
    def load_faults(root: Path) -> pd.DataFrame:
        """Load CoreOps fault-injection ground truth."""
        with (root / "labels/fault_labels.json").open(encoding="utf-8") as f:
            return pd.json_normalize(json.load(f)["run_history"])

    @staticmethod
    def summarize_logs(root: Path) -> pd.DataFrame:
        """Summarize operational log severity by network function."""

        pattern = re.compile(r"\[[^\]]+\]\s+(INFO|WARNING|WARN|ERROR|DEBUG|FATAL|CRITICAL):")
        results = []

        for path in sorted((root / "logs").glob("*.log")):
            counts = Counter()

            with path.open(encoding="utf-8", errors="replace") as f:
                for line in f:
                    match = pattern.search(line)
                    if match:
                        counts[match.group(1)] += 1

            total = sum(counts.values())
            warnings = counts["WARNING"] + counts["WARN"]
            errors = counts["ERROR"] + counts["FATAL"] + counts["CRITICAL"]

            results.append({
                "nf": path.stem,
                "events": total,
                "info": counts["INFO"],
                "warnings": warnings,
                "errors": errors,
                "warning_error_pct": round(100 * (warnings + errors) / total, 2) if total else 0
            })

        return pd.DataFrame(results)

    @staticmethod
    def summarize_availability(root: Path) -> pd.DataFrame:
        """Summarize UP/DOWN observations for each network function."""

        counts = defaultdict(Counter)
        path = root / "metrics/global_matrix.csv"

        with path.open(encoding="utf-8") as f:
            next(f, None)

            for line in f:
                fields = line.strip().split(";")

                for field in fields[1:]:
                    if not field:
                        continue

                    if "=" not in field:
                        raise ValueError(f"Invalid NF status field: {field}")

                    nf, status = field.split("=", 1)
                    counts[nf.strip()][status.strip().upper()] += 1

        results = []

        for nf, states in sorted(counts.items()):
            up, down = states["UP"], states["DOWN"]
            total = sum(states.values())

            results.append({
                "nf": nf,
                "observations": total,
                "up": up,
                "down": down,
                "other_states": total - up - down,
                "down_pct": round(100 * down / (up + down), 2) if up + down else 0
            })

        return pd.DataFrame(results)

    @staticmethod
    def summarize_metrics(root: Path) -> pd.DataFrame:
        """Summarize operational metric coverage and variability."""

        results = []
        metrics_dir = root / "metrics/per_nf0525"

        for path in sorted(metrics_dir.glob("*.csv")):
            df = pd.read_csv(path, sep=";", low_memory=False)
            numeric = df.select_dtypes(include="number")

            scrape = (
                pd.to_numeric(df["scrape_ok"], errors="coerce")
                if "scrape_ok" in df else None
            )

            restart = (
                pd.to_numeric(df["restart_detected"], errors="coerce")
                if "restart_detected" in df else None
            )

            results.append({
                "nf": path.stem.split("_")[0],
                "rows": len(df),
                "columns": len(df.columns),
                "numeric_columns": len(numeric.columns),
                "variable_numeric_columns": int(numeric.nunique(dropna=True).gt(1).sum()),
                "scrape_failures": int(scrape.eq(0).sum()) if scrape is not None else None,
                "restart_flags": int(restart.eq(1).sum()) if restart is not None else None
            })

            del df

        return pd.DataFrame(results)

    @staticmethod
    def check_temporal_consistency(root: Path) -> pd.DataFrame:
        """Check temporal evidence coverage for CoreOps fault records."""

        timezone_name = "Asia/Shanghai"  # UTC+08:00
        faults = CoreOps.load_faults(root)
        windows = pd.read_json(root / "metrics/aligned_fault_window.json")

        # 1. Match ground truth with fault windows
        matched = faults.merge(
            windows,
            on="fault_id",
            how="left",
            suffixes=("", "_window"),
            indicator=True,
            validate="one_to_one"
        )

        for column in ["start_time", "end_time", "start_time_window", "end_time_window"]:
            matched[column] = pd.to_datetime(
                matched[column], utc=True, errors="coerce"
            ).dt.tz_convert(timezone_name)

        years = matched["start_time"].dt.year.dropna().unique()
        if len(years) != 1:
            raise ValueError("Log year cannot be inferred unambiguously.")

        year = int(years[0])

        # 2. Index Open5GS log timestamps
        pattern = re.compile(r"^(\d{2}/\d{2} \d{2}:\d{2}:\d{2}\.\d+):")
        log_times = {}

        for path in sorted((root / "logs").glob("*.log")):
            timestamps = []

            with path.open(encoding="utf-8", errors="replace") as f:
                for line in f:
                    match = pattern.match(line)
                    if match:
                        timestamps.append(f"{year}/{match.group(1)}")

            parsed = pd.to_datetime(
                timestamps,
                format="%Y/%m/%d %H:%M:%S.%f",
                errors="coerce"
            )

            log_times[path.stem] = (
                pd.DatetimeIndex(parsed)
                .tz_localize(timezone_name)
                .dropna()
                .sort_values()
            )

        # 3. Load global NF availability
        records = []

        with (root / "metrics/global_matrix.csv").open(encoding="utf-8") as f:
            next(f, None)

            for line in f:
                fields = line.strip().split(";")

                record = {"timestamp": fields[0]}

                for field in fields[1:]:
                    if "=" in field:
                        nf, status = field.split("=", 1)
                        record[nf.strip()] = status.strip().upper()

                records.append(record)

        matrix = pd.DataFrame(records)

        matrix["timestamp"] = pd.to_datetime(
            matrix["timestamp"], errors="coerce"
        ).dt.tz_localize(timezone_name)

        matrix = (
            matrix.dropna(subset=["timestamp"])
            .set_index("timestamp")
            .sort_index()
        )

        # 4. Index selected per-NF metrics
        metric_times = {}

        for path in sorted((root / "metrics/per_nf0525").glob("*.csv")):
            df = pd.read_csv(path, sep=";", usecols=["timestamp", "scrape_ok"])

            timestamps = pd.DatetimeIndex(
                pd.to_datetime(df["timestamp"], errors="coerce")
            )

            timestamps = (
                timestamps.tz_localize(timezone_name)
                if timestamps.tz is None
                else timestamps.tz_convert(timezone_name)
            )

            valid = timestamps.notna()
            successful = pd.to_numeric(
                df["scrape_ok"], errors="coerce"
            ).eq(1).to_numpy()

            metric_times[path.stem.split("_")[0]] = {
                "all": timestamps[valid].sort_values(),
                "successful": timestamps[valid & successful].sort_values()
            }

        # 5. Count observations inside each fault window
        def count_in_window(index, start, end) -> int:
            return int(
                index.searchsorted(end, side="right")
                - index.searchsorted(start, side="left")
            )

        results = []

        for _, row in matched.iterrows():
            start, end = row["start_time"], row["end_time"]
            targets = row["targets"]
            nf = targets[0] if isinstance(targets, list) and len(targets) == 1 else None

            label_match = bool(
                row["_merge"] == "both"
                and row["fault_type"] == row["fault_type_window"]
                and row["targets"] == row["targets_window"]
                and start == row["start_time_window"]
                and end == row["end_time_window"]
            )

            if pd.isna(start) or pd.isna(end):
                raise ValueError(f"Invalid fault window: {row['fault_id']}")

            states = matrix.loc[start:end, nf] if nf in matrix.columns else None
            logs = log_times.get(nf)
            metrics = metric_times.get(nf)

            results.append({
                "fault_id": row["fault_id"],
                "fault_type": row["fault_type"],
                "nf": nf,
                "label_window_match": label_match,
                "log_events": (
                    count_in_window(logs, start, end)
                    if logs is not None else pd.NA
                ),
                "global_observations": (
                    int(states.notna().sum()) if states is not None else pd.NA
                ),
                "global_down": (
                    int(states.eq("DOWN").sum()) if states is not None else pd.NA
                ),
                "metric_samples": (
                    count_in_window(metrics["all"], start, end)
                    if metrics is not None else pd.NA
                ),
                "successful_scrapes": (
                    count_in_window(metrics["successful"], start, end)
                    if metrics is not None else pd.NA
                )
            })

        return pd.DataFrame(results)