from pydantic import BaseModel


class TraderBase(BaseModel):
    username: str
    email: str
    first_name: str
    last_name: str
    is_superuser: bool = False


class TraderPrivate(TraderBase):
    hashed_password: str


class TraderCreate(TraderBase):
    pass


class Trader(TraderBase):
    id: int
