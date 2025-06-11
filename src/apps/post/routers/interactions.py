from fastapi import APIRouter
from fastapi import Depends
from src.core.db import get_db

router = APIRouter()

@router.post("/like/{post_id}")
async def add_like_to_post(post_id: int, db=Depends(get_db)):
    return {"message": "Hello, World!"}

@router.post("/comment/{post_id}")
async def add_comment_to_post(post_id: int, db=Depends(get_db)):
    return {"message": "Hello, World!"}