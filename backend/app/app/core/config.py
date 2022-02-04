from secrets import token_urlsafe

from pydantic import BaseSettings, PostgresDsn


class Settings(BaseSettings):
    SQLALCHEMY_DATABASE_URL: PostgresDsn = "postgresql://user:password@127.0.0.1/app"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24  # 60 minutes * 24 hours = 1 day
    SECRET_KEY: str = token_urlsafe(64)
    ALGORITHM: str = "HS256"


settings = Settings()
