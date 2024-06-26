import os
from pathlib import Path

from pydantic_settings import BaseSettings

BASE_DIR = Path(__file__).parent.parent


class Setting(BaseSettings):
    api_v1_prefix: str = "/api/v1"
    db_echo: bool = True
    db_url: str = os.getenv("DATABASE_URL", "postgresql+asyncpg://rich_trader:__rich_trader__1337@192.168.0.2:5432/trader_db")


settings = Setting()
