from pydantic import BaseModel
from datetime import datetime


class Message(BaseModel):
    id: int
    body: str
    date_create: datetime


class MessageInDB(Message):
    id: int