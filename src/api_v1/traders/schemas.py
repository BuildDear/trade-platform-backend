from pydantic import BaseModel
from sqlalchemy.orm import Mapped



class Trader(BaseModel):
    email: str
    password: str
    name: str
    surname: str
