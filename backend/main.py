from fastapi import FastAPI
from backend.core.config import settings
from backend.api.routes.base import api_router
from backend.db.session import engine
from backend.db.base import Base

def include_router(app):
  app.include_router(api_router)

def create_tables():
	Base.metadata.create_all(bind=engine)

def start_application():
  app = FastAPI(title=settings.PROJECT_NAME,version=settings.PROJECT_VERSION)
  include_router(app)
  create_tables()
  return app

app = start_application()

