from typing import Generator

from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from jose import JWTError, jwt

from app.db.session import SessionLocal
from app.models import User
from app.core.config import settings
from app.crud import crud_user
from app.exceptions import exceptions

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login/access-token")


def get_db() -> Generator:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_current_user(
    db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)
) -> User:
    try:
        payload = jwt.decode(
            token=token, key=settings.SECRET_KEY, algorithms=[settings.ALGORITHM]
        )
    except JWTError:
        raise exceptions.CREDENTIALS_EXCEPTION
    else:
        username = payload.get("sub")
        user_obj = crud_user.get_by_username(db=db, username=username)
        if not user_obj:
            raise exceptions.CREDENTIALS_EXCEPTION
        return user_obj
