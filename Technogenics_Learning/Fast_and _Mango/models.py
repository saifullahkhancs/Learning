from pydantic import BaseModel , Field
from typing import Optional
from bson import ObjectId


class Student(BaseModel):
    name: str
    phone_number : str | None= None

class StudentResponce(BaseModel):

    id: Optional[str] = None  # ObjectId will be converted to string
    name: str
    phone_number : str | None

    class Config:
         json_encoders = {
            ObjectId: str  # Automatically converts ObjectId to string
        }
    