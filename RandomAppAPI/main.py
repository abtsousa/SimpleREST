from fastapi import FastAPI

from RandomAppAPI.routers.suggest_app import router as suggest_app

app = FastAPI()

app.include_router(suggest_app, prefix="/suggest_app")
