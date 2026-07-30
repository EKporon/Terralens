import os
from dotenv import load_dotenv

load_dotenv()


class Config:

    PROJECT_NAME = "TerraLens"

    DEBUG = True

    SECRET_KEY = os.getenv(
        "SECRET_KEY",
        "terralens-development-key"
    )

    NOMINATIM_URL = (
        "https://nominatim.openstreetmap.org/search"
    )

    WEATHER_URL = (
        "https://api.open-meteo.com/v1/forecast"
    )

    ELEVATION_URL = (
        "https://api.open-elevation.com/api/v1/lookup"
    )
