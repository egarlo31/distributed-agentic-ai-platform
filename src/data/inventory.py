from pathlib import Path


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
        """Return the file extensions present in the raw data directory."""

        extensions = {
            file.suffix.lower()
            for file in self.raw_data_path.iterdir()
            if file.is_file() and file.suffix
        }

        if not extensions:
            raise ValueError(
                f"No file extensions were found in: {self.raw_data_path}"
            )

        return extensions