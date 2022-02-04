from datetime import datetime, timedelta

from jose import jwt
from passlib.hash import bcrypt_sha256

from app.core.config import settings


def create_access_token(sub: str) -> str:
    claims = {
        "sub": sub,
        "exp": datetime.utcnow() + timedelta(
            minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
        )
    }
    access_token = jwt.encode(
        claims=claims, key=settings.SECRET_KEY, algorithm=settings.ALGORITHM
    )
    return access_token


def get_hashed_password(password: str) -> str:
    return bcrypt_sha256.hash(secret=password)


def verify_password(password, hashed_password) -> bool:
    return bcrypt_sha256.verify(secret=password, hash=hashed_password)
