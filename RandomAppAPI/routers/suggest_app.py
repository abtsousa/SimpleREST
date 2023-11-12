from fastapi import APIRouter, HTTPException
from RandomAppAPI.models.appinfo import AppInfo, AppsList
from pydantic import ValidationError
import random


APPS_LIST = [
    "Evony: The King's Return",
    "Lords Mobile: Kingdom Wars",
    "Clash of Clans",
]  # Hard-coded list.


router = APIRouter()


def get_random_app_name(apps: AppsList = AppsList(app_name_list=APPS_LIST)) -> str:
    """
    Auxiliary method that returns a random app name from a list of app name strings.

    Args:
        apps (AppsList): list of app names to choose from. (optional)
                          Defaults to the hard-coded list APPS_LIST.
    """
    return random.choice(apps.app_name_list)


@router.get("/suggest_app", response_model=AppInfo, summary="Suggest an app")
async def suggest_app() -> AppInfo:
    """
    Suggests a random app from the available apps list in the store.
    """
    try:
        return AppInfo(app_name=get_random_app_name())
    except (
        AttributeError,
        ValidationError,
    ) as e:  # Check for invalid list and return 400 Bad Request
        raise HTTPException(
            status_code=400, detail=": ".join([type(e).__name__, str(e)])
        )
