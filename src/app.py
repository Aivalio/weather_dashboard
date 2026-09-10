"""Streamlit UI for the Weather Dashboard."""
import sys
from pathlib import Path

# Make project root importable when running `streamlit run src/app.py`
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import streamlit as st
from src.services.weather_fetcher import WeatherFetcher
from src.services.visualizer import DataVisualizer
from src.services.history_tracker import HistoryTracker


# --- Page config ---
st.set_page_config(
    page_title="Weather Dashboard",
    page_icon="🌤️",
    layout="wide"
)

st.title("🌤️ Weather Forecast for the Next Days")

# --- Session state ---
if "tracker" not in st.session_state:
    st.session_state.tracker = HistoryTracker()
if "place" not in st.session_state:
    st.session_state.place = ""

tracker: HistoryTracker = st.session_state.tracker

# --- Sidebar: search history ---
with st.sidebar:
    st.header("Recent searches")
    history = tracker.load()
    if history:
        for city in history:
            if st.button(city, key=f"history_{city}", use_container_width=True):
                st.session_state.place = city
                st.rerun()
        if st.button("Clear history", type="secondary", use_container_width=True):
            tracker.clear()
            st.rerun()
    else:
        st.caption("No searches yet.")

# --- Main inputs ---
place = st.text_input("Place:", value=st.session_state.place)
days = st.slider("Forecast Days", min_value=1, max_value=5,
                 help="Select the number of forecasted days")
option = st.selectbox("Select data to view", ("Temperature", "Sky"))

# --- Fetch and display ---
if place:
    st.subheader(f"{option} for the next {days} days in {place}")
    try:
        fetcher = WeatherFetcher()
        forecasts = fetcher.get_forecast(place, days)

        # Record search
        if place != st.session_state.place:
            tracker.add(place)
            st.session_state.place = place

        if option == "Temperature":
            figure = DataVisualizer.temperature_chart(forecasts)
            st.plotly_chart(figure, use_container_width=True)
        else:  # Sky
            image_paths = DataVisualizer.sky_image_paths(forecasts)
            cols = st.columns(min(len(image_paths), 8))
            for i, path in enumerate(image_paths):
                with cols[i % 8]:
                    st.image(path, width=115)

    except ValueError as e:
        st.error(f"⚠️ {e}")
    except Exception as e:
        st.error(f"Something went wrong: {e}")