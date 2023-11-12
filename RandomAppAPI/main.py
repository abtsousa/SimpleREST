# Imports
from fastapi import FastAPI  # FastAPI

from RandomAppAPI.routers.suggest_app import router as suggest_app  # Our API

# App metadata
__author__ = "Afonso Bras Sousa"
__maintainer__ = "Afonso Bras Sousa"
__version__ = "0.1.0"

description = """
RandomApp API is a simple API that suggests an app from a list of available apps.

Currently supports suggesting one of the following three apps:

    - "Evony: The King's Return"
    - "Lords Mobile: Kingdom Wars"
    - "Clash of Clans"
"""


# Initialize the API
app = FastAPI(
    title="RandomApp API",
    description=description,
    summary="Suggest a random app.",
    version="0.1.0",
    contact={
        "name": "Afonso Bras Sousa",
    },
)

# Include our suggest_app APIRouter
app.include_router(suggest_app)
