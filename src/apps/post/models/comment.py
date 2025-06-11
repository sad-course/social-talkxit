from sqlmodel import Field, SQLModel
from datetime import datetime
from src.apps.post.utils import current_time

class CommentModel(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True, description="Unique identifier for the comment")
    content: str = Field(max_length=1000, description="Content of the comment")
    author_id: int = Field(nullable=False, description="ID of the author of the comment")
    post_id: int = Field(foreign_key="postmodel.id", nullable=True, description="ID of the post to which this comment belongs")
    created_at: datetime = Field(default_factory=current_time, nullable=True, description="Timestamp when the comment was created")
    updated_at: datetime = Field(default_factory=current_time, nullable=True, description="Timestamp when the comment was last updated")