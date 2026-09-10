"""Configuration loader for environment variables."""
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


def get_api_key() -> str:
    """Retrieve OpenWeatherMap API key from environment variables.

    Returns:
        str: The API key.

    Raises:
        ValueError: If OPENWEATHER_API_KEY is not set.
    """
    api_key = os.getenv("OPENWEATHER_API_KEY")
    if not api_key:
        raise ValueError(
            "OPENWEATHER_API_KEY not set. "
            "Copy .env.example to .env and add your key."
        )
    return api_key