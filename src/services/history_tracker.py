"""Search history tracker for weather dashboard."""
import json
from pathlib import Path


class HistoryTracker:
    """Stores and retrieves the last N searched cities in a JSON file."""

    MAX_ENTRIES = 5

    def __init__(self, filepath: str = "data/history.json"):
        """Initialize tracker with a JSON file path.

        Args:
            filepath: Path to the JSON file used for persistence.
        """
        self.filepath = Path(filepath)
        self.filepath.parent.mkdir(parents=True, exist_ok=True)

    def load(self) -> list[str]:
        """Load the search history from disk.

        Returns:
            List of city names (most recent first).
        """
        if not self.filepath.exists():
            return []
        try:
            with self.filepath.open("r", encoding="utf-8") as f:
                data = json.load(f)
            return data if isinstance(data, list) else []
        except (json.JSONDecodeError, OSError):
            return []

    def add(self, city: str) -> list[str]:
        """Add a city to the history, keeping only the last N entries.

        If the city already exists, it is moved to the top.

        Args:
            city: City name to record.

        Returns:
            Updated history list.
        """
        city = city.strip()
        if not city:
            return self.load()

        history = self.load()
        history = [c for c in history if c.lower() != city.lower()]
        history.insert(0, city)
        history = history[: self.MAX_ENTRIES]

        self._save(history)
        return history

    def clear(self) -> None:
        """Delete the history file."""
        if self.filepath.exists():
            self.filepath.unlink()

    def _save(self, history: list[str]) -> None:
        """Persist history to disk."""
        with self.filepath.open("w", encoding="utf-8") as f:
            json.dump(history, f, ensure_ascii=False, indent=2)