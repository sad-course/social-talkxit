from sqlmodel import create_engine
from src.config.settings import settings

connect_args = {"check_same_thread": False} if "sqlite" in settings.database_url else {}

engine = create_engine(settings.database_url, connect_args=connect_args)
print(f"Connecting to database at {settings.database_url}")

def get_engine():
    return engine