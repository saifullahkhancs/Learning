from pydantic import BaseModel , Field
from typing import Optional
from bson import ObjectId


class Log(BaseModel):
    log_level: str
    message: str
    source: str
    timestamp: str

class LogSearch(BaseModel):
    # log_level: Optional[str] = Field(None, example="INFO")
    # start_timestamp: Optional[str] = Field(None, example="2023-10-20T12:00:00Z")
    # end_timestamp: Optional[str] = Field(None, example="2023-10-21T12:00:00Z")
    # message_value: Optional[str] = Field(None, example="Application started successfully")
    log_level: Optional[str] = None
    start_timestamp: Optional[int] = None
    end_timestamp: Optional[int] = None
    message_value: Optional[str] = None

class LogResponce(BaseModel):

    id: Optional[str] = None  # ObjectId will be converted to string
    name: str
    phone_number : str | None

    class Config:
         json_encoders = {
            ObjectId: str  # Automatically converts ObjectId to string
        }
    