from fastapi import APIRouter
from ..types import Post

router = APIRouter()

@router.post("/post", response_model=Post)
def create_post():
    return {"message": "Hello, World!"}

