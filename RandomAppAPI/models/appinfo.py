from pydantic import BaseModel


class AppInfo(BaseModel):
    app_name: str
