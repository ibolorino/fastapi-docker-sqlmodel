from typing import Optional

from pydantic import EmailStr
from sqlmodel import Field, SQLModel


class UserBase(SQLModel):
    id: Optional[int] = Field(default=None, primary_key=True)
    email: EmailStr
    full_name: str


class User(UserBase, table=True):
    password: str
    is_active: bool = True
    is_superuser: bool = False


class UserRead(UserBase):
    id: int
    is_active: bool
    is_superuser: bool


class UserCreate(UserBase):
    password: str
    confirm_password: str


class UserUpdate(UserBase):
    full_name: Optional[str]
