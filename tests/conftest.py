"""Shared pytest fixtures."""
import pytest


@pytest.fixture
def sample_forecasts():
    """Return a minimal list of forecast entries mimicking the API response."""
    return [
        {
            "dt_txt": "2026-09-10 12:00:00",
            "main": {"temp": 24.5},
            "weather": [{"main": "Clear"}],
        },
        {
            "dt_txt": "2026-09-10 15:00:00",
            "main": {"temp": 26.1},
            "weather": [{"main": "Clouds"}],
        },
        {
            "dt_txt": "2026-09-10 18:00:00",
            "main": {"temp": 22.0},
            "weather": [{"main": "Rain"}],
        },
    ]