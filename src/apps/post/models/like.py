from sqlmodel import Field, SQLModel, UniqueConstraint
from datetime import datetime

def current_time():
    """Retorna o horário atual com fuso horário UTC."""
    return datetime.utcnow()

class LikeModel(SQLModel, table = True):
    __table_args__ = (
        UniqueConstraint("author_id", "post_id", name="uix_author_post_like"),
    )
     
    id: int | None = Field(default=None, primary_key=True, description="Unique identifier for the like")
    author_id: int = Field(nullable=False, description="ID of the author of the post")
    post_id: int = Field(foreign_key="postmodel.id", nullable=False, description="ID of the liked post")
    status: bool = Field(default=True, description= "True if the user liked the post, False if unliked")
    created_at: datetime = Field(default_factory=current_time, nullable=True, description="Timestamp when the like was created")
    updated_at: datetime = Field(default_factory=current_time, nullable=True, description="Timestamp when the like was last updated")
