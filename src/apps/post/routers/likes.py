from fastapi import APIRouter, HTTPException
from fastapi import Depends
from fastapi import Request
from sqlalchemy import and_, select
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.middleware import auth_required
from src.apps.post.models import Post as PostModel
from src.apps.post.models.like import LikeModel
from src.apps.post.schemas.like import LikeCreate, LikeRead
from src.core.db import get_db

router = APIRouter()

