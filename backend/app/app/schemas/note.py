from typing import Optional, List

from pydantic import BaseModel, Field, constr


class NoteBase(BaseModel):
    title: Optional[str] = Field(
        default=None,
        description="Note title",
        min_length=3,
        max_length=64,
    )
    content: Optional[str] = Field(
        default=None, description="Note content", max_length=1048576,
    )
    tags: List[constr(max_length=16)] = Field(
        default=[],
        description="Note tags",
        max_items=8
    )


class NoteRead(NoteBase):
    class Config:
        orm_mode = True


class NoteCreate(NoteBase):
    title: str = Field(
        default=...,
        description="Note title",
        min_length=3,
        max_length=32,
    )


class NoteUpdate(NoteBase):
    ...


class NoteInDB(NoteBase):
    owner_id: int
