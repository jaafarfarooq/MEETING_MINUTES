from fastapi import APIRouter
from api.api_v1.endpoints import routes

api_router = APIRouter()
api_router.include_router(routes.router, tags=["upload"])
