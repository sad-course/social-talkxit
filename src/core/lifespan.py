import logging
from contextlib import asynccontextmanager
from fastapi import FastAPI
from src.core.db import create_db_and_tables, dispose_engine

@asynccontextmanager
async def lifespan(app: FastAPI):
    try:
        await create_db_and_tables()
        yield
    except Exception as e:
        logging.exception("Erro durante o startup da aplicação")
        raise
    finally:
        await dispose_engine()