from fastapi import FastAPI
from app.api import router
from app.db.base import Base, engine

app = FastAPI()

app.include_router(router)

# Create tables
Base.metadata.create_all(bind=engine)
