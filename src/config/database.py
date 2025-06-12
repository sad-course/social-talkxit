from src.config.settings import settings

from sqlalchemy.ext.asyncio import create_async_engine
connect_args = {"check_same_thread": False} if "sqlite" in settings.database_url else {}

engine = create_async_engine(settings.database_url, connect_args=connect_args)

def get_engine():
    return engine