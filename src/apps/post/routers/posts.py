from fastapi import APIRouter
from fastapi import Depends
from fastapi import Request
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.middleware import auth_required
from ..types import Post as PostDTO
from src.apps.post.models import PostModel
from src.core.db import get_db
router = APIRouter()

@router.get("/post", description="List all posts")
async def list_posts(db : AsyncSession=Depends(get_db)):
    async with db as session:
        result = await session.execute(select(PostModel).order_by(PostModel.created_at.desc()))
    
        posts = result.scalars().all()

        return posts


@router.post("/post", description="Create a new post")
@auth_required
async def create_post(request: Request, post: PostDTO, db: AsyncSession = Depends(get_db)):
    async with db as session:
        post_model = PostModel(**post.model_dump())

        post_model.author_id = request.state.user.get('user_id')
        session.add(post_model)
        await session.commit()
        await session.refresh(post_model)
        return post_model
    

