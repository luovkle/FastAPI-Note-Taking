from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.api.deps import get_db, get_current_user
from app.schemas import UserCreate, UserRead, UserUpdate
from app.crud import crud_user
from app.models import User

router = APIRouter()


@router.post(path="", response_model=UserRead)
def create_user(db: Session = Depends(get_db), *, user_create: UserCreate):
    user_obj = crud_user.create(db=db, user_create=user_create)
    return user_obj


@router.get(path="/me", response_model=UserRead)
def get_user(current_user: User = Depends(get_current_user)):
    return current_user


@router.patch(path="/me", response_model=UserRead)
def update_user(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
    *,
    user_update: UserUpdate
):
    user_obj = crud_user.update(
        db=db, username=current_user.username, user_update=user_update
    )
    return user_obj


@router.delete(path="/me", response_model=UserRead)
def delete_user(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    user_obj = crud_user.delete(db=db, username=current_user.username)
    return user_obj
