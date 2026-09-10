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

        Raises:
            ValueError: If city not found or API key invalid.
            requests.RequestException: For network errors.
        """
        params = {
            "q": place,
            "appid": self.api_key,
            "units": "metric",
        }

        try:
            response = requests.get(self.BASE_URL, params=params, timeout=10)
        except requests.Timeout:
            raise requests.RequestException(
                "The weather service took too long to respond. Try again."
            )
        except requests.ConnectionError:
            raise requests.RequestException(
                "Could not connect to the weather service. Check your internet."
            )

        if response.status_code == 404:
            raise ValueError(f"City '{place}' not found. Check the spelling.")
        if response.status_code == 401:
            raise ValueError("Invalid API key. Check your .env file.")

        response.raise_for_status()

        data = response.json()
        forecasts = data["list"]
        max_entries = days * 8
        return forecasts[:max_entries]