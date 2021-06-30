from fastapi import FastAPI
from core.config import settings
from api.routes.home import general_pages_router
from db.session import engine
from db.base import Base

def include_router(app):
  app.include_router(general_pages_router)

def create_tables():
	Base.metadata.create_all(bind=engine)

def start_application():
  app = FastAPI(title=settings.PROJECT_NAME,version=settings.PROJECT_VERSION)
  include_router(app)
  create_tables()
  return app

app = start_application()

