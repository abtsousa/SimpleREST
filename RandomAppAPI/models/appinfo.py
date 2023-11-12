from pydantic import BaseModel, Field


class AppInfo(BaseModel):
    """
    A simple app info model.
    """
    app_name: str = Field(description="The app's name.")
