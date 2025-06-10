from fastapi import APIRouter

router = APIRouter()

@router.post("/like/{post_id}")
def add_like_to_post(post_id: int):
    return {"message": "Hello, World!"}

@router.post("/comment/{post_id}")
def add_comment_to_post(post_id: int):
    return {"message": "Hello, World!"}