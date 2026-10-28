"""Locate approved raw datasets and inventory source files without mutation."""
from pathlib import Path
import pandas as pd


class DataInventory:
    """Locate and inspect the raw files associated with a data source."""

    def __init__(self,source_id: str,start: Path | None = None,) -> None:
        self.source_id = source_id
        self.start = (start or Path.cwd()).resolve()

        self.project_root = self._find_project_root()
        self.raw_data_path = self._find_raw_data_path()

    def _find_project_root(self) -> Path:
        """Locate the project root using the Git repository marker."""

        for directory in (self.start, *self.start.parents):
            if (directory / ".git").exists():
                return directory

        raise FileNotFoundError(
            "Project root could not be located."
        )

    def _find_raw_data_path(self) -> Path:
        raw_dir = self.project_root / "data" / "raw"

        if not raw_dir.is_dir():
            raise FileNotFoundError(f"Raw data directory not found: {raw_dir}")

        matches = [
            path for path in raw_dir.iterdir()
            if path.is_dir() and path.name.startswith(self.source_id)
        ]

        if not matches:
            raise FileNotFoundError(f"No raw data found for {self.source_id}")

        if len(matches) > 1:
            raise RuntimeError(f"Multiple raw sources found: {matches}")

        return matches[0]

    def discover_file_extensions(self) -> set[str]:
        """Discover file extensions recursively within the data source."""
        return {
            path.suffix.lower()
            for path in self.raw_data_path.rglob("*")
            if path.is_file() and path.suffix and path.name != "README.md"
        }

    def file_inventory(self) -> pd.DataFrame:
        """Return a recursive inventory of the raw data files."""

        records = []

        for path in self.raw_data_path.rglob("*"):
            if not path.is_file():
                continue

            relative_path = path.relative_to(self.raw_data_path)

            if path.name == "README.md" or any(
                    part.startswith(".") for part in relative_path.parts
            ):
                continue

            records.append({
                "file": path.name,
                "relative_path": relative_path.as_posix(),
                "extension": path.suffix.lower() or "(none)",
                "size_bytes": path.stat().st_size
            })

        return pd.DataFrame(
            records,
            columns=["file", "relative_path", "extension", "size_bytes"]
        ).sort_values("relative_path").reset_index(drop=True)