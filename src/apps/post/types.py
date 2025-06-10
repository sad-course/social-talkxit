from pydantic import BaseModel, Field

class Post(BaseModel):
    id: int = Field(..., description="Unique identifier for the post")
    title: str = Field(..., description="Title of the post")
    content: str = Field(..., description="Content of the post")
    author_id: int = Field(..., description="ID of the author of the post")
    created_at: str = Field(..., description="Timestamp when the post was created")
    updated_at: str = Field(..., description="Timestamp when the post was last updated")
    is_published: bool = Field(..., description="Indicates whether the post is published")
    tags: list[str] = Field(default_factory=list, description="List of tags associated with the post")


class PostUpdate(BaseModel):
    title: str | None = Field(None, description="Updated title of the post")
    content: str | None = Field(None, description="Updated content of the post")