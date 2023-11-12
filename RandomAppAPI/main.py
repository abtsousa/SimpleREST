from fastapi import FastAPI
from pydantic import BaseModel
import random


APPS_LIST = ["Evony: The King's Return", "Lords Mobile: Kingdom Wars", "Clash of Clans"] # Hard-coded list.


app = FastAPI()


class AppInfo(BaseModel):
    app_name: str


def get_random_app_name(apps=APPS_LIST) -> str:
    """
    Auxiliary method that returns a random app name from a list of app name strings.

    Args:
        apps (List[str]): list of app names to choose from (optional)
                          Defaults to the hard-coded list APPS_LIST.
    """
    return random.choice(apps)



@app.get("/suggest_app", response_model=AppInfo)
async def suggest_app():
    return {"app_name": get_random_app_name()}
