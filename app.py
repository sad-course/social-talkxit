from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.apps.post.routers.interactions import router as interaction_router
from src.apps.post.routers.posts import router as post_router

def create_app() -> FastAPI:
    app = FastAPI()

    # Add CORS middleware to allow requests from any origin
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],  # Allows all origins
        allow_credentials=True,
        allow_methods=["*"],  # Allows all methods (GET, POST, etc.)
        allow_headers=["*"],  # Allows all headers
    )

    return app

app = create_app()

app.include_router(post_router, prefix="/api", tags=["posts"])
app.include_router(interaction_router, prefix="/api", tags=["interactions"])