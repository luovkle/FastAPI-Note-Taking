from typing import Optional

from sqlalchemy.orm import Session

from app.models import User
from app.schemas import UserCreate, UserInDB, UserUpdate
from app.core.security import get_hashed_password, verify_password
from app.exceptions import exceptions
from .crud_note import crud_note


class CRUDUser:
    def get_by_username(self, db: Session, username: str) -> Optional[User]:
        return db.query(User).filter(User.username == username).first()

    def get_by_email(self, db: Session, email: str) -> Optional[User]:
        return db.query(User).filter(User.email == email).first()

    def create(self, db: Session, user_create: UserCreate) -> User:
        if self.get_by_username(db=db, username=user_create.username):
            raise exceptions.USERNAME_UNAVAILABLE
        if self.get_by_email(db=db, email=user_create.email):
            raise exceptions.EMAIL_UNAVAILABLE
        user_in_db = UserInDB(
            **user_create.dict(),
            hashed_password=get_hashed_password(password=user_create.password)
        )
        user_obj = User(**user_in_db.dict())
        db.add(user_obj)
        db.commit()
        db.refresh(user_obj)
        return user_obj

    def update(self, db: Session, username: str, user_update: UserUpdate) -> User:
        user_obj = self.get_by_username(db=db, username=username)
        if not user_obj:
            raise exceptions.CREDENTIALS_EXCEPTION
        user_in_db = UserInDB(
            **user_update.dict(),
            hashed_password=get_hashed_password(password=user_update.password)
            if user_update.password
            else None
        )
        user_in_db_dict = user_in_db.dict(exclude_none=True)
        for field in user_in_db_dict:
            setattr(user_obj, field, user_in_db_dict[field])
        db.add(user_obj)
        db.commit()
        db.refresh(user_obj)
        return user_obj

    def delete(self, db: Session, username: str) -> User:
        user_obj = self.get_by_username(db=db, username=username)
        if not user_obj:
            raise exceptions.CREDENTIALS_EXCEPTION
        crud_note.delete_by_owner_id(db=db, owner_id=user_obj.id)
        db.delete(user_obj)
        db.commit()
        return user_obj

    def authenticate(self, db: Session, username: str, password: str) -> User:
        user_obj = self.get_by_username(db=db, username=username)
        if not user_obj:
            raise exceptions.CREDENTIALS_EXCEPTION
        if not verify_password(
            password=password, hashed_password=user_obj.hashed_password
        ):
            raise exceptions.CREDENTIALS_EXCEPTION
        return user_obj


crud_user = CRUDUser()
