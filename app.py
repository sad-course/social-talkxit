from fastapi import FastAPI
from src.core.lifespan import lifespan
from src.core.middleware import setup_middlewares
from src.core.router import setup_routes

app = FastAPI(lifespan=lifespan)

# Configura middlewares
setup_middlewares(app)

# Configura rotas
setup_routes(app)