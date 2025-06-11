from sqlmodel import Field, SQLModel
from datetime import datetime

class Post(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True, description="Unique identifier for the post")
    content: str = Field(max_length=1000, description="Content of the post")
    author_id: int = Field(nullable=False, description="ID of the author of the post")
    created_at: datetime = Field(default=None, nullable=True, description="Timestamp when the post was created")
    updated_at: datetime = Field(default=None, nullable=True, description="Timestamp when the post was last updated")
    is_published: bool = Field(default=False, description="Indicates whether the post is published")
 
