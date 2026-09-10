"""Visualization service for weather forecast data."""
from typing import Any
import plotly.express as px
import plotly.graph_objects as go


class DataVisualizer:
    """Creates Plotly charts from OpenWeatherMap forecast data."""

    # Mapping of weather conditions to local image paths
    SKY_IMAGES: dict[str, str] = {
        "Clear": "images/clear.png",
        "Clouds": "images/cloud.png",
        "Rain": "images/rain.png",
        "Snow": "images/snow.png",
    }

    @staticmethod
    def temperature_chart(forecasts: list[dict[str, Any]]) -> go.Figure:
        """Build a line chart of temperature over time.

        Args:
            forecasts: List of forecast entries from the API.

        Returns:
            Plotly Figure object.
        """
        temperatures = [entry["main"]["temp"] for entry in forecasts]
        dates = [entry["dt_txt"] for entry in forecasts]

        figure = px.line(
            x=dates,
            y=temperatures,
            labels={"x": "Date", "y": "Temperature (°C)"},
            title="Temperature Forecast",
        )
        figure.update_traces(line_color="#ff7f0e", line_width=3)
        return figure

    @classmethod
    def sky_image_paths(cls, forecasts: list[dict[str, Any]]) -> list[str]:
        """Map weather conditions to local image paths.

        Args:
            forecasts: List of forecast entries from the API.

        Returns:
            List of image file paths.
        """
        conditions = [entry["weather"][0]["main"] for entry in forecasts]
        return [
            cls.SKY_IMAGES.get(condition, "images/cloud.png")
            for condition in conditions
        ]