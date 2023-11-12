from pydantic import BaseModel


class AppInfo(BaseModel):
    """
    A simple app info model.

    Parameters:
        app_name (str): The app's name.
    """
    app_name: str
