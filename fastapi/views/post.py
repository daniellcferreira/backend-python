from datetime import datetime
from pydantic import BaseModel


class PostOut(BaseModel):
    title: str
    content: str
    published_at: datetime | None = None
