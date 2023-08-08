from typing import Optional

from sqlmodel import Field, SQLModel


class BrandBase(SQLModel):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str


class Brand(BrandBase, table=True):
    pass


class BrandRead(BrandBase):
    id: int


class BrandCreate(BrandBase):
    pass


class BrandUpdate(BrandBase):
    name: Optional[str]
