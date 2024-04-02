import os
import asyncio
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL")

if not SQLALCHEMY_DATABASE_URL:
    raise ValueError("DATABASE_URL is not set")

# Створюємо асинхронний механізм
async_engine = create_async_engine(SQLALCHEMY_DATABASE_URL, future=True, echo=True)

# Створюємо фабрику асинхронних сесій
async_session = async_sessionmaker(async_engine, expire_on_commit=False, class_=AsyncSession, future=True)

Base = declarative_base()

# Вивід повідомлення про успішне підключення
async def main():
    async with async_engine.connect() as conn:
        print("Connected to database successfully.")

# Запускаємо main() асинхронно
asyncio.run(main())
