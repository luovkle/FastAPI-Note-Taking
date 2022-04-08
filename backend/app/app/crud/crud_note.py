from typing import List, Optional

from sqlalchemy import and_
from sqlalchemy.orm import Session

from app.models import Note
from app.schemas import NoteCreate, NoteUpdate, NoteInDB
from app.exceptions import exceptions
from app.utils import generate_zip_file


class CRUDNote:
    def get_by_title(self, db: Session, owner_id: int, title: str) -> Optional[Note]:
        return (
            db.query(Note)
            .filter(and_(Note.owner_id == owner_id, Note.title == title))
            .first()
        )

    def get_by_owner_id(self, db: Session, owner_id: int) -> List[Note]:
        return db.query(Note).filter(Note.owner_id == owner_id).all()

    def get_by_keyword_in_title(
        self, db: Session, owner_id: int, title: str
    ) -> List[Note]:
        return (
            db.query(Note)
            .filter(and_(Note.owner_id == owner_id, Note.title.contains(title)))
            .all()
        )

    def get_by_tag(self, db: Session, owner_id: int, tag: str) -> List[Note]:
        return (
            db.query(Note)
            .filter(and_(Note.owner_id == owner_id, Note.tags.any(tag)))
            .all()
        )

    def get_by_title_and_tag(
        self, db: Session, owner_id: int, title: str, tag: str
    ) -> List[Note]:
        return (
            db.query(Note)
            .filter(
                and_(
                    Note.owner_id == owner_id,
                    and_(Note.title.contains(title), Note.tags.any(tag)),
                )
            )
            .all()
        )

    def create(self, db: Session, owner_id: int, note_create: NoteCreate) -> Note:
        if self.get_by_title(db=db, owner_id=owner_id, title=note_create.title):
            raise exceptions.TITLE_UNAVAILABLE
        note_in_db = NoteInDB(**note_create.dict(), owner_id=owner_id)
        note_obj = Note(**note_in_db.dict())
        db.add(note_obj)
        db.commit()
        db.refresh(note_obj)
        return note_obj

    def update(
        self, db: Session, owner_id: int, current_title: str, note_update: NoteUpdate
    ) -> Note:
        note_obj = self.get_by_title(db=db, owner_id=owner_id, title=current_title)
        if not note_obj:
            raise exceptions.NOTE_NOT_FOUND
        if self.get_by_title(db=db, owner_id=owner_id, title=note_update.title):
            raise exceptions.TITLE_UNAVAILABLE
        note_in_db = NoteInDB(**note_update.dict(exclude_unset=True), owner_id=owner_id)
        note_in_db_dict = note_in_db.dict(exclude_unset=True)
        for field in note_in_db_dict:
            # if field in note_obj.__dict__:
            setattr(note_obj, field, note_in_db_dict[field])
        db.add(note_obj)
        db.commit()
        db.refresh(note_obj)
        return note_obj

    def delete(self, db: Session, owner_id: int, title: str) -> Note:
        note_obj = self.get_by_title(db=db, owner_id=owner_id, title=title)
        if not note_obj:
            raise exceptions.NOTE_NOT_FOUND
        db.delete(note_obj)
        db.commit()
        return note_obj

    def delete_by_owner_id(self, db: Session, owner_id: int) -> List[Note]:
        notes = self.get_by_owner_id(db=db, owner_id=owner_id)
        for note in notes:
            db.delete(note)
        db.commit()
        return notes

    def export(self, db: Session, owner_id: int) -> str:
        notes = self.get_by_owner_id(db=db, owner_id=owner_id)
        file = generate_zip_file(notes=notes)
        return file


crud_note = CRUDNote()
