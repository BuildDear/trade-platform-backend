import os
from pydantic_settings import BaseSettings


class Setting(BaseSettings):

    api_v1_prefix: str = "/api/v1"
    db_echo: bool = True
    db_url: str = os.getenv("DATABASE_URL")


settings = Setting()
