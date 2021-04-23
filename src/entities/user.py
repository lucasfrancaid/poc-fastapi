from pydantic import BaseModel
from typing import Optional


class User(BaseModel):
    id: Optional[int] = 0
    name: str
    email: str
    phone: Optional[str] = None

