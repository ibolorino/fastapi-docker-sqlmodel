from typing import Optional

from pydantic import condecimal
from sqlmodel import Field, SQLModel


class ProductBase(SQLModel):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    price: condecimal(max_digits=8, decimal_places=2)


class Product(ProductBase, table=True):
    pass


class ProductRead(ProductBase):
    id: int


class ProductCreate(ProductBase):
    pass


class ProductUpdate(ProductBase):
    name: Optional[str]
    price: Optional[condecimal(max_digits=8, decimal_places=2)]
