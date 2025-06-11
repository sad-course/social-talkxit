from pydantic import BaseModel, Field
from datetime import datetime

class Post(BaseModel):
    content: str = Field(..., description="Content of the post")
    is_published: bool | None = Field(..., description="Indicates whether the post is published")
