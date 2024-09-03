from pydantic import BaseModel
from typing import Optional


class Student(BaseModel):
    name: str
    phone_number : str | None= None