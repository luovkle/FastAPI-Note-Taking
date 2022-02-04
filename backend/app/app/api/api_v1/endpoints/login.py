from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.api.deps import get_db
from app.crud import crud_user
from app.core.security import create_access_token
from app.schemas import Token

router = APIRouter()


@router.post(path="/access-token", response_model=Token)
def login(
    db: Session = Depends(get_db),
    form_data: OAuth2PasswordRequestForm = Depends()
):
    user = crud_user.authenticate(
        db=db, username=form_data.username, password=form_data.password
    )
    access_token = create_access_token(sub=user.username)
    return {"access_token": access_token, "token_type": "Bearer"}
