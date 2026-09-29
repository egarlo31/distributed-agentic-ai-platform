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
        """Locate the directory associated with the data source."""

        excluded_dirs = {
            ".git",
            ".venv",
            "__pycache__",
            ".ipynb_checkpoints",
        }

        matches = [
            directory
            for directory in self.project_root.rglob("*")
            if directory.is_dir()
               and not any(part in excluded_dirs for part in directory.parts)
               and directory.name.lower().startswith(self.source_id.lower())
        ]

        if not matches:
            raise FileNotFoundError(
                f"No data directory found for {self.source_id}."
            )

        if len(matches) > 1:
            raise RuntimeError(
                f"Multiple directories found for {self.source_id}: {matches}"
            )

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