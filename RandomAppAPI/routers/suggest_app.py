from fastapi import APIRouter
from RandomAppAPI.models.appinfo import AppInfo
import random


APPS_LIST = [
    "Evony: The King's Return",
    "Lords Mobile: Kingdom Wars",
    "Clash of Clans",
]  # Hard-coded list.


router = APIRouter()


def get_random_app_name( apps: list[str] = APPS_LIST ) -> str:
    """
    Auxiliary method that returns a random app name from a list of app name strings.

    Args:
        apps (List[str]): list of app names to choose from. (optional)
                          Defaults to the hard-coded list APPS_LIST.
    """
    return random.choice(apps)


@router.get("/suggest_app", response_model=AppInfo, summary="Suggest an app")
async def suggest_app() -> AppInfo:
    """
    Suggests a random app from the available apps list in the store.
    """
    return AppInfo(app_name=get_random_app_name())
