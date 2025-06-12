from pydantic import BaseModel
from enum import Enum
from datetime import datetime

class LikeCreate(BaseModel):
    author_id: int
    post_id: int
    status: bool

class LikeRead(BaseModel):
    id: int
    author_id: int
    post_id: int
    status: bool
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True