from typing import TYPE_CHECKING, List, Optional

from sqlmodel import Field, Relationship, SQLModel

if TYPE_CHECKING:
    from .product import Product, ProductRead


class BrandBase(SQLModel):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str


class Brand(BrandBase, table=True):
    products: List["Product"] = Relationship(back_populates="brand")


class BrandRead(BrandBase):
    id: int


class BrandReadWithProducts(BrandRead):
    products: List["ProductRead"] = []


class BrandCreate(BrandBase):
    pass


class BrandUpdate(BrandBase):
    name: Optional[str]
