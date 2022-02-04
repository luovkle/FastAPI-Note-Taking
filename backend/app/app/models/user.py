from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String(16), unique=True, nullable=False)
    email = Column(String(254), unique=True, nullable=False)
    hashed_password = Column(String(512), nullable=False)
    notes = relationship("Note", backref="owner")

    def __init__(self, username: str, email: str, hashed_password: str) -> None:
        self.username = username
        self.email = email
        self.hashed_password = hashed_password

    def __repr__(self) -> str:
        return f"<User {self.username}>"
