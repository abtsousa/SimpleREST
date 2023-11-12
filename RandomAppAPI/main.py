from fastapi import FastAPI
import random


app = FastAPI()


def get_random_app_name() -> str:
    """Auxiliary method that returns a random app name from a hard-coded list."""
    apps = ["Evony: The King's Return", "Lords Mobile: Kingdom Wars", "Clash of Clans"] # The hard-coded list.
    return random.choice(apps)



@app.get("/suggest_app")
async def suggest_app():
    return {"app_name": get_random_app_name()}
