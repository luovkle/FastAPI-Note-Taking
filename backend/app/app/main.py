from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.api.api_v1.api import api_router
from app.core.config import settings

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.PROJECT_VERSION,
    docs_url=settings.DOCS_URL,
    redoc_url=settings.REDOC_URL,
)
app.include_router(router=api_router, prefix=settings.API_STR)
app.mount(
    settings.STATIC_URL, StaticFiles(directory=settings.STATIC_DIR), name="static"
)
