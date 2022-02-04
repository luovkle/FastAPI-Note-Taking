from typing import List, Optional

from fastapi import APIRouter, Depends, Query, Path
from sqlalchemy.orm import Session

from app.api.deps import get_current_user, get_db
from app.crud import crud_note
from app.models import User
from app.schemas import NoteCreate, NoteRead, NoteUpdate

router = APIRouter()


@router.post(path="", response_model=NoteRead)
def create_note(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
    *,
    note_create: NoteCreate
):
    note_obj = crud_note.create(
        db=db, owner_id=current_user.id, note_create=note_create
    )
    return note_obj


@router.get(path="", response_model=List[NoteRead])
def get_notes(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
    title: Optional[str] = Query(default=None),
    tag: Optional[str] = Query(default=None)
):
    if title and tag:
        notes = crud_note.get_by_title_and_tag(db, current_user.id, title, tag)
    elif title:
        notes = crud_note.get_by_keyword_in_title(db, current_user.id, title)
    elif tag:
        notes = crud_note.get_by_tag(db, current_user.id, tag)
    else:
        notes = crud_note.get_by_owner_id(db, current_user.id)
    return notes


@router.patch(path="/{title}", response_model=NoteRead)
def update_note(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
    title: str = Path(default=..., description="Note title"),
    *,
    note_update: NoteUpdate
):
    note_obj = crud_note.update(
        db=db, owner_id=current_user.id, current_title=title, note_update=note_update
    )
    return note_obj


@router.delete(path="/{title}", response_model=NoteRead)
def delete_note(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
    title: str = Path(default=..., description="Note title")
):
    note_obj = crud_note.delete(db=db, owner_id=current_user.id, title=title)
    return note_obj
