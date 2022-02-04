from fastapi import APIRouter

from app.api.api_v1.endpoints import users, notes, login

api_router = APIRouter()
api_router.include_router(router=login.router, prefix="/login", tags=["login"])
api_router.include_router(router=users.router, prefix="/users", tags=["users"])
api_router.include_router(router=notes.router, prefix="/notes", tags=["notes"])
