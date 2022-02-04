from typing import List

from sqlalchemy import Column, String, Integer, ForeignKey, Text, ARRAY

from app.db.base_class import Base


class Note(Base):
    __tablename__ = "notes"

    id = Column(Integer, primary_key=True)
    owner_id = Column(Integer, ForeignKey("users.id"))
    title = Column(String(64), nullable=False)
    content = Column(Text)
    tags = Column(ARRAY(String(16)))

    def __init__(
        self, owner_id: int, title: str, content: str = None, tags: List[str] = []
    ) -> None:
        self.owner_id = owner_id
        self.title = title
        self.content = content
        self.tags = tags

    def __repr__(self) -> str:
        return f"<Note {self.title}>"
