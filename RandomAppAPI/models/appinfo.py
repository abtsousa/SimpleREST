from pydantic import BaseModel, Field


class AppInfo(BaseModel):
    """
    A simple app info model.
    """
    app_name: str = Field(description="The app's name.")


class AppsList(BaseModel):
    """
    A list of app names (strings).
    """
    app_name_list : list[str] = Field(description="The list of app names.")
