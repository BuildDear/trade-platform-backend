from pydantic import BaseModel


class TraderBase(BaseModel):
    email: str
    password: str
    name: str
    surname: str


class TraderCreate(TraderBase):
    pass


class Trader(TraderBase):
    id: int
