from sqlalchemy.orm import Mapped
from src.database.base_model import Base


class Trader(Base):
    name: Mapped[str]