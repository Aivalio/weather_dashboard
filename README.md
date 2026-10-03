<div align="center">

# 🌤️ Weather Dashboard

**A clean, OOP-based weather forecast dashboard built with Streamlit.**

[![Python](https://img.shields.io/badge/Python-3.11+-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-FF4B4B?logo=streamlit&logoColor=white)](https://streamlit.io/)
[![Plotly](https://img.shields.io/badge/Plotly-5.17+-3F4F75?logo=plotly&logoColor=white)](https://plotly.com/)
[![Tests](https://github.com/Aivalio/weather_dashboard/actions/workflows/tests.yml/badge.svg)](https://github.com/Aivalio/weather_dashboard/actions/workflows/tests.yml) 
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

[**🚀 Live Demo**](https://weatherdashboard-5nyksu68u8jgfbekbcxy8m.streamlit.app/) · [**🐛 Report Bug**](https://github.com/Aivalio/weather_dashboard/issues) · [**✨ Request Feature**](https://github.com/Aivalio/weather_dashboard/issues)

</div>

---

## 📖 About

A Streamlit dashboard that fetches real-time weather forecasts from the OpenWeatherMap API.
Built as a **learning project** to practice clean architecture, testing, deployment,
and proper Git workflow (feature branches + atomic commits).

**The focus was not on flashy UI — it was on writing code that is easy to read, test, and extend.**

---

## ✨ Features

| Feature | Description |
|---|---|
| 🔍 **City Search** | Look up any city worldwide |
| 📅 **5-Day Forecast** | Slider to select 1–5 days ahead |
| 📈 **Temperature Chart** | Interactive Plotly line chart in °C |
| 🌤️ **Sky Conditions** | Icon-based visualization (Clear, Clouds, Rain, Snow) |
| 🕒 **Search History** | Last 5 cities, persisted to JSON, one-click rerun |
| 🛡️ **Error Handling** | Friendly messages for 404, 401, timeouts |
| ⚙️ **Configurable** | API key loaded from `.env` — never hardcoded |

---

## 🏗️ Architecture

The project follows the **Single Responsibility Principle**:



**Why this matters:**
- **Fetcher** knows nothing about UI or charts.
- **Visualizer** knows nothing about HTTP or files.
- **Tracker** knows nothing about weather.
- Everything is **independently testable** (and mocked in tests).

---

## 🛠️ Tech Stack

| Layer | Technology | Purpose |
|---|---|---|
| **UI** | Streamlit | Rapid interactive dashboards |
| **HTTP** | Requests | OpenWeatherMap API calls |
| **Charts** | Plotly Express | Interactive temperature graph |
| **Config** | python-dotenv | Secure secrets management |
| **Tests** | pytest + pytest-mock | Unit tests with mocked API |
| **Deploy** | Streamlit Cloud | Free hosting from GitHub |

---

## 🚀 Live Demo

👉 **[weather-dashboard.streamlit.app](https://weatherdashboard-5nyksu68u8jgfbekbcxy8m.streamlit.app/)**

> Try searching for your city and switching between **Temperature** and **Sky** views.

---

## 📦 Installation

### Prerequisites

- Python 3.11+
- A free [OpenWeatherMap API key](https://openweathermap.org/api)

### 1. Clone the repository

```bash
git clone https://github.com/Aivalio/weather_dashboard.git
cd weather_dashboard
```


### 2. Create a virtual environment

```bash
python -m venv .venv

# Windows (PowerShell)
.venv\Scripts\Activate.ps1

# macOS / Linux
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure secrets

```bash
# Windows
Copy-Item .env.example .env

# macOS / Linux
cp .env.example .env
```

Edit `.env` and add your key:

```
OPENWEATHER_API_KEY=your_actual_key_here
```

> ⚠️ **Never commit `.env`.** It is ignored by Git.

### 5. Run the app

```bash
streamlit run src/app.py
```

Open http://localhost:8501

---

## 🧪 Testing

```bash
pytest tests/ -v
```

**Coverage:**

| Module | What's tested |
|---|---|
| `WeatherFetcher` | API key handling, response trimming, error codes (404/401/timeout) |
| `DataVisualizer` | Chart generation, icon mapping, fallback for unknown conditions |
| `HistoryTracker` | Persistence, deduplication (case-insensitive), 5-entry cap, clear |

All tests use **`pytest-mock`** — no real HTTP calls are made.

---

## 📁 Project Structure

```
weather-dashboard/
├── src/
│   ├── __init__.py
│   ├── app.py                       # Streamlit UI entry point
│   ├── config.py                    # Loads env vars via dotenv
│   └── services/
│       ├── __init__.py
│       ├── weather_fetcher.py       # OpenWeatherMap API client
│       ├── visualizer.py            # Plotly chart + sky icon mapper
│       └── history_tracker.py       # JSON-based search history
├── tests/
│   ├── __init__.py
│   ├── conftest.py                  # Shared fixtures
│   ├── test_weather_fetcher.py
│   ├── test_visualizer.py
│   └── test_history_tracker.py
├── images/                          # Sky condition icons
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

---

## 🗺️ Roadmap

- [ ] Cache API responses per city with `@st.cache_data`
- [ ] Hourly view for the next 24 hours
- [ ] Export search history as CSV
- [ ] Dockerize for self-hosting
- [ ] Add more languages (i18n)

---

## 🤝 Contributing

This is a personal learning project, but suggestions are welcome.
Feel free to open an issue or fork the repo.

---

## 📄 License

Distributed under the **MIT License**. See `LICENSE` for more information.

---

<div align="center">

**Built with ☕ and curiosity by [Aivalio](https://github.com/Aivalio)**

⭐ If you found this useful, consider giving it a star!

</div>