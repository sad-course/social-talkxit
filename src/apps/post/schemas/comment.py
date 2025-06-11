from pydantic import BaseModel, Field

class CommentSchema(BaseModel):
    content: str = Field(..., description="Content of the post")