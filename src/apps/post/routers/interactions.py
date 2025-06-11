from fastapi import APIRouter, HTTPException
from fastapi import Depends
from fastapi import Request
from sqlalchemy import and_, select
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.middleware import auth_required
from src.apps.post.models.post import PostModel
from src.apps.post.models.like import LikeModel
from src.apps.post.schemas.like import LikeCreate, LikeRead
from src.core.db import get_db

router = APIRouter()

@router.post("/post/{post_id}/like", description="Like or unlike a post")
@auth_required
async def give_like(
    request: Request, 
    like: LikeCreate,  
    post_id: int, 
    db: AsyncSession = Depends(get_db)
):
    user_id = request.state.user.get("user_id")

    async with db as session:
        post = await session.get(PostModel, post_id)
        if not post:
            raise HTTPException(status_code=404, detail="Post not found")
        
        result = await session.execute(
            select(PostModel).where(
                and_(
                    LikeModel.author_id == user_id,
                    LikeModel.post_id == post_id,
                )
            )
        )

        existing_like = result.scalars().first()

        if existing_like:
            existing_like.status = like.status
            await session.commit()
            await session.refresh(existing_like)
            return existing_like
        
        new_like = LikeModel(
            author_id=user_id,
            post_id=post_id,
            status=like.status
        )

        session.add(new_like)
        await session.commit()
        await session.refresh(new_like)
        return new_like
    
@router.delete("/like/{like_id}", description="Remove a like")
@auth_required
async def remove_like(
    like_id: int,
    request: Request,
    db: AsyncSession = Depends(get_db)
):
    user_id = request.state.user.get("user_id")

    async with db as session:
        like = await session.get(LikeModel, like_id)
        if not like:
            raise HTTPException(status_code=404, detail="Like not found")
        if like.author_id != user_id:
            raise HTTPException(status_code=403, detail="Not authorized to delete this like")

        await session.delete(like)
        await session.commit()
        return {"detail": "Like deleted"}
    
@router.get("/post/{post_id}/likes", response_model=list[LikeRead], description="List likes of a post")
async def get_likes_for_post(
    post_id: int,
    db: AsyncSession = Depends(get_db)
):
    async with db as session:
        result = await session.execute(
            select(LikeModel).where(LikeModel.post_id == post_id)
        )
        likes = result.scalars().all()
        return likes

@router.post("/comment/{post_id}")
async def add_comment_to_post(post_id: int, db=Depends(get_db)):
    return {"message": "Hello, World!"}