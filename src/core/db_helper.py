from asyncio import current_task
from sqlalchemy.ext.asyncio import (
    AsyncSession,
    create_async_engine,
    async_sessionmaker,
    async_scoped_session
)
from src.core.config import settings


# Клас DatabaseHelper створює асинхронний двигун SQLAlchemy та фабрику сесій
class DatabaseHelper:
    def __init__(self, url: str, echo: bool = False):
        # Створюємо асинхронний двигун SQLAlchemy
        self.engine = create_async_engine(
            url=url,
            echo=echo,
        )
        # Створюємо фабрику сесій, яка прив'язана до двигуна
        self.session_factory = async_sessionmaker(
            bind=self.engine,
            autoflush=False,
            autocommit=False,
            expire_on_commit=False,
        )

    # Створюємо область дії сесії, яка прив'язана до поточного завдання asyncio
    def get_scoped_session(self):
        session = async_scoped_session(
            session_factory=self.session_factory,
            scopefunc=current_task,
        )
        return session

    # Створюємо сесію, повертаємо її, а потім закриваємо, коли генератор вичерпаний
    async def session_dependency(self) -> AsyncSession:
        async with self.session_factory() as session:
            yield session
            await session.close()

    # Створюємо сесію з областю дії, повертаємо її, а потім закриваємо, коли генератор вичерпаний
    async def scoped_session_dependency(self) -> AsyncSession:
        session = self.get_scoped_session()
        yield session
        await session.close()


# Створюємо екземпляр DatabaseHelper з URL бази даних та параметром echo з конфігурації додатку
db_helper = DatabaseHelper(
    url=settings.db_url,
    echo=settings.db_echo,
)
