from fastapi import FastAPI
from core.config import settings
from apis.app_router import page_router


from db.base import Base
from db.session import engine

def include_router(app):
    app.include_router(page_router)

def create_tables():
    Base.metadata.create_all(bind=engine)

def start_app():
    app = FastAPI(title=settings.PROJECT_NAME, version=settings.PROJECT_VERSION)
    include_router(app)
    create_tables()
    return app

app = start_app()