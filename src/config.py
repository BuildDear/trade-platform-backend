import os
from pathlib import Path
from pydantic_settings import BaseSettings

BASE_DIR = Path(__file__).parent.parent
SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL")

class Setting(BaseSettings):
    api_v1_prefix: str = "/api/v1"

    db_url: str = SQLALCHEMY_DATABASE_URL
    db_echo: bool = False
    # db_echo: bool = True


settings = Setting()