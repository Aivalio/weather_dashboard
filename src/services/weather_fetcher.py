"""Weather data fetcher using OpenWeatherMap API."""
from typing import Any
import requests
from src.config import get_api_key


class WeatherFetcher:
    """Fetches weather forecast data from OpenWeatherMap."""

    BASE_URL = "https://api.openweathermap.org/data/2.5/forecast"

    def __init__(self, api_key: str | None = None):
        """Initialize fetcher with API key.

        Args:
            api_key: OpenWeatherMap API key. If None, loads from environment.
        """
        self.api_key = api_key or get_api_key()

    def get_forecast(self, place: str, days: int = 1) -> list[dict[str, Any]]:
        """Fetch forecast for a place.

        Args:
            place: City name.
            days: Number of days (1-5).

        Returns:
            List of forecast entries (raw API data, every 3 hours).
        """
        params = {
            "q": place,
            "appid": self.api_key,
            "units": "metric",
        }
        response = requests.get(self.BASE_URL, params=params, timeout=10)
        response.raise_for_status()

        data = response.json()
        forecasts = data["list"]
        max_entries = days * 8
        return forecasts[:max_entries]