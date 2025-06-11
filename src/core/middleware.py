from functools import wraps
from fastapi.middleware.cors import CORSMiddleware
from fastapi import Request, HTTPException
from fastapi.responses import RedirectResponse


from jose import jwt, JWTError
from datetime import datetime

from src.config.settings import settings


def setup_middlewares(app):
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],  # Allows all origins
        allow_credentials=True,
        allow_methods=["*"],  # Allows all methods (GET, POST, etc.)
        allow_headers=["*"],  # Allows all headers
    )


def auth_required(func):
    """
    Decorator to ensure that a request has a valid JWT token.
    This is a placeholder for actual JWT validation logic.
    """
    @wraps(func)
    async def wrapper(request: Request, *args, **kwargs):

        authorization: str = request.headers.get("Authorization")
        if not authorization or not authorization.startswith("Bearer "):
            raise HTTPException(status_code=401, detail="Token de autenticação não fornecido")

        token = authorization.split(" ")[1]
        try:
            payload = jwt.decode(token, settings.jwt_secret_key, algorithms=[settings.jwt_algorithm])
            exp = payload.get("exp")
            if exp and datetime.utcfromtimestamp(exp) < datetime.utcnow():
                return RedirectResponse(url=f"{settings.auth_api_base}/token/refresh")
            request.state.user = payload
        except JWTError as exc:
            raise HTTPException(status_code=401, detail="Token inválido")

        return await func(request, *args, **kwargs)
    
    return wrapper