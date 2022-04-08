import os
from secrets import token_urlsafe
from typing import Optional

from pydantic import BaseSettings, PostgresDsn, AnyHttpUrl


class Settings(BaseSettings):
    PROJECT_NAME: str = "FastAPI Note Taking"
    PROJECT_VERSION: str = "1.0"
    DOCS_URL: str = "/docs"
    REDOC_URL: Optional[str] = None
    API_STR: str = "/api/v1"
    URL_BASE: AnyHttpUrl = "http://127.0.0.1:8000"
    STATIC_DIR: str = "static"
    STATIC_URL: str = "/static"
    POSTGRES_USER: str = os.getenv("POSTGRES_USER")
    POSTGRES_PASSWORD: str = os.getenv("POSTGRES_PASSWORD")
    POSTGRES_SERVER: str = os.getenv("POSTGRES_SERVER")
    POSTGRES_DB: str = os.getenv("POSTGRES_DB")
    SQLALCHEMY_DATABASE_URL: PostgresDsn = (
        f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}/"
        f"{POSTGRES_DB}"
    )
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24  # 60 minutes * 24 hours = 1 day
    SECRET_KEY: str = token_urlsafe(64)
    ALGORITHM: str = "HS256"


settings = Settings()
