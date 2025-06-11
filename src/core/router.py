from fastapi import FastAPI
from src.apps.post.routers.interactions import router as interaction_router
from src.apps.post.routers.posts import router as post_router

def setup_routes(app: FastAPI):
    app.include_router(post_router, prefix="/api", tags=["posts"])
    app.include_router(interaction_router, prefix="/api", tags=["interactions"])