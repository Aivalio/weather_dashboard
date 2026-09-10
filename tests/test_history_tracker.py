"""Tests for HistoryTracker."""
import json
from pathlib import Path

from src.services.history_tracker import HistoryTracker


def test_load_returns_empty_when_file_missing(tmp_path):
    tracker = HistoryTracker(filepath=str(tmp_path / "history.json"))
    assert tracker.load() == []


def test_add_keeps_most_recent_first(tmp_path):
    tracker = HistoryTracker(filepath=str(tmp_path / "history.json"))
    tracker.add("Athens")
    tracker.add("London")
    assert tracker.load() == ["London", "Athens"]


def test_add_does_not_duplicate_cities(tmp_path):
    tracker = HistoryTracker(filepath=str(tmp_path / "history.json"))
    tracker.add("Athens")
    tracker.add("London")
    tracker.add("Athens")  # case-insensitive duplicate
    assert tracker.load() == ["Athens", "London"]


def test_add_keeps_only_max_entries(tmp_path):
    tracker = HistoryTracker(filepath=str(tmp_path / "history.json"))
    for city in ["A", "B", "C", "D", "E", "F"]:
        tracker.add(city)
    assert tracker.load() == ["F", "E", "D", "C", "B"]


def test_clear_removes_file(tmp_path):
    filepath = tmp_path / "history.json"
    tracker = HistoryTracker(filepath=str(filepath))
    tracker.add("Athens")
    assert filepath.exists()
    tracker.clear()
    assert not filepath.exists()