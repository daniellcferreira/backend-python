from datetime import datetime
from pydantic import BaseModel


class PostOut(BaseModel):
    title: str
    date: datetime
