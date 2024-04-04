from sqlalchemy.orm import Mapped
from src.core.models.base_model import Base


class Trader(Base):
    email: Mapped[str]
    password: Mapped[str]
    name: Mapped[str]
    surname: Mapped[str]
