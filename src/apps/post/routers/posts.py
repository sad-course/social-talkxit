from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from ..types import Post as PostDTO
from src.apps.post.models import Post as PostModel
from src.core.db import get_db

router = APIRouter()

@router.get("/post", description="List all posts")
async def list_posts(db : AsyncSession=Depends(get_db)):
    async with db as session:
        result = await session.execute(select(PostModel).order_by(PostModel.created_at.desc()))
    
        posts = result.scalars().all()

        return posts


@router.post("/post", description="Create a new post")
async def create_post(post: PostDTO, db: AsyncSession = Depends(get_db)):
    async with db as session:
        post_model = PostModel(**post.model_dump())
        session.add(post_model)
        await session.commit()
        await session.refresh(post_model)
        return post_model
    

