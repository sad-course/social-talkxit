from sqlmodel import SQLModel

from src.config.database import get_engine
from src.apps.post.models import *

engine = get_engine()

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def dispose_engine():
    engine.dispose()