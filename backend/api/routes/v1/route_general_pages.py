from fastapi import APIRouter
from fastapi import Request

general_pages_router = APIRouter()

@general_pages_router.get("/")
async def home(request: Request):
  return {"msg":"Hello API"}