"""Inspect source schemas, missingness and quality without changing raw values."""
import json
from itertools import islice
from pathlib import Path

import pandas as pd

class Schema:
    """Preview JSON, text and CSV schemas for source assessment."""


    def __init__(self, nrows: int = 50) -> None:
        self.nrows = nrows

    @staticmethod
    def inspect_json_schema(path: Path, records_key: str) -> dict:
        """Inspect JSON root fields and nested record fields."""
        with path.open(encoding="utf-8") as f:
            data = json.load(f)

        records = data[records_key]

        return {
            "root_fields": list(data),
            "record_fields": list(records[0]) if records else []
        }

    @staticmethod
    def preview_text(path: Path, n: int = 3) -> list[str]:
        """Read the first lines of a text file."""
        with path.open(encoding="utf-8", errors="replace") as f:
            return [line.rstrip("\n") for line in islice(f, n)]

    def inspect_csv_schema(self, path: Path, sep: str = ",") -> pd.DataFrame:
        """Inspect CSV columns and preliminary inferred data types."""
        df = pd.read_csv(path, sep=sep, nrows=self.nrows)

        return pd.DataFrame({
            "column": df.columns,
            "dtype": df.dtypes.astype(str).values
        })

class Quality:
    """Compute dataset quality summaries and validate fault-label consistency."""


    @staticmethod
    def profile_dataframe(df: pd.DataFrame, name: str, unique_key: str | None = None) -> dict:
        """Compute basic data quality statistics."""

        rows, columns = df.shape
        missing = int(df.isna().sum().sum())

        return {
            "dataset": name,
            "rows": rows,
            "columns": columns,
            "missing_values": missing,
            "missing_pct": round(missing / (rows * columns) * 100, 2) if rows * columns else 0,
            "duplicates": int(df.duplicated(subset=[unique_key] if unique_key else None).sum())
        }

    @staticmethod
    def validate_faults(faults: pd.DataFrame) -> pd.DataFrame:
        """Validate fault timestamps, durations, and targets."""

        start = pd.to_datetime(faults["start_time"], utc=True, errors="coerce")
        end = pd.to_datetime(faults["end_time"], utc=True, errors="coerce")
        duration = pd.to_numeric(faults["duration_sec"], errors="coerce")

        checks = {
            "Missing fault IDs": faults["fault_id"].isna().sum(),
            "Missing targets": faults["targets"].apply(
                lambda x: not isinstance(x, list) or not x
            ).sum(),
            "Invalid timestamps": (start.isna() | end.isna()).sum(),
            "Invalid intervals": (end <= start).sum(),
            "Invalid durations": (duration.isna() | (duration <= 0)).sum(),
            "Duration mismatches": (
                    ((end - start).dt.total_seconds() - duration).abs() > 1
            ).sum()
        }

        return pd.DataFrame(
            checks.items(),
            columns=["check", "invalid_records"]
        )