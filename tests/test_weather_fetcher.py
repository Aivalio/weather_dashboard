"""Tests for WeatherFetcher."""
import pytest
import requests
from unittest.mock import MagicMock

from src.services.weather_fetcher import WeatherFetcher


def test_fetcher_uses_provided_api_key():
    """The provided key should override the env variable."""
    fetcher = WeatherFetcher(api_key="test_key_123")
    assert fetcher.api_key == "test_key_123"


def test_get_forecast_returns_limited_entries(mocker, sample_forecasts):
    """get_forecast should trim to days * 8 entries."""
    fake_response = MagicMock()
    fake_response.status_code = 200
    fake_response.json.return_value = {"list": sample_forecasts * 10}
    fake_response.raise_for_status = MagicMock()

    mocker.patch("requests.get", return_value=fake_response)

    fetcher = WeatherFetcher(api_key="fake")
    result = fetcher.get_forecast("Athens", days=1)

    assert len(result) == 8  # 1 day * 8 entries


def test_get_forecast_raises_on_404(mocker):
    """A 404 should raise ValueError with a helpful message."""
    fake_response = MagicMock()
    fake_response.status_code = 404

    mocker.patch("requests.get", return_value=fake_response)

    fetcher = WeatherFetcher(api_key="fake")
    with pytest.raises(ValueError, match="not found"):
        fetcher.get_forecast("FakeCity")


def test_get_forecast_raises_on_401(mocker):
    """A 401 should raise ValueError mentioning the API key."""
    fake_response = MagicMock()
    fake_response.status_code = 401

    mocker.patch("requests.get", return_value=fake_response)

    fetcher = WeatherFetcher(api_key="bad")
    with pytest.raises(ValueError, match="Invalid API key"):
        fetcher.get_forecast("Athens")


def test_get_forecast_raises_on_timeout(mocker):
    """Timeout should become a RequestException with a friendly message."""
    mocker.patch("requests.get", side_effect=requests.Timeout)

    fetcher = WeatherFetcher(api_key="fake")
    with pytest.raises(requests.RequestException, match="took too long"):
        fetcher.get_forecast("Athens")