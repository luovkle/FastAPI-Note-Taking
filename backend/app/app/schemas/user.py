from typing import Optional

from pydantic import BaseModel, Field, EmailStr


class UserBase(BaseModel):
    username: Optional[str] = Field(
        default=None,
        description="Account username",
        min_length=3,
        max_length=16,
    )
    email: Optional[EmailStr] = Field(
        default=None,
        description="Account email",
    )


class UserRead(UserBase):
    class Config:
        orm_mode = True


class UserCreate(UserBase):
    username: str = Field(
        default=...,
        description="Account username",
        min_length=3,
        max_length=16,
    )
    email: EmailStr = Field(
        default=...,
        description="Account email",
    )
    password: str = Field(
        default=...,
        description="Account password",
        min_length=14,
        max_length=512
    )


class UserUpdate(UserBase):
    password: Optional[str] = Field(
        default=None,
        description="Account password",
        min_length=14,
        max_length=512
    )


class UserInDB(UserBase):
    hashed_password: Optional[str]
