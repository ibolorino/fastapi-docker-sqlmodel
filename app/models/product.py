from typing import TYPE_CHECKING, Optional

from pydantic import condecimal
from sqlmodel import Field, Relationship, SQLModel

if TYPE_CHECKING:
    from .brand import Brand, BrandRead


class ProductBase(SQLModel):
    name: str
    price: condecimal(max_digits=8, decimal_places=2)


class Product(ProductBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    brand_id: Optional[int] = Field(default=None, foreign_key="brand.id")
    brand: Optional["Brand"] = Relationship(back_populates="products")


class ProductRead(ProductBase):
    id: int
    brand_id: int


class ProductReadWithBrand(ProductRead):
    brand: Optional["BrandRead"] = None


class ProductCreate(ProductBase):
    brand_id: int


class ProductUpdate(ProductBase):
    name: Optional[str]
    price: Optional[condecimal(max_digits=8, decimal_places=2)]
