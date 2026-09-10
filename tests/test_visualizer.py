"""Tests for DataVisualizer."""
from src.services.visualizer import DataVisualizer


def test_temperature_chart_returns_figure(sample_forecasts):
    figure = DataVisualizer.temperature_chart(sample_forecasts)
    assert len(figure.data) == 1
    assert list(figure.data[0].y) == [24.5, 26.1, 22.0]


def test_sky_image_paths_maps_known_conditions(sample_forecasts):
    paths = DataVisualizer.sky_image_paths(sample_forecasts)
    assert paths == [
        "images/clear.png",
        "images/cloud.png",
        "images/rain.png",
    ]


def test_sky_image_paths_falls_back_on_unknown_condition():
    forecasts = [{"weather": [{"main": "Fog"}]}]
    paths = DataVisualizer.sky_image_paths(forecasts)
    assert paths == ["images/cloud.png"]