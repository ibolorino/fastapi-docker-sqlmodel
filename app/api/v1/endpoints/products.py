from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select

from app.api.v1.dependencies import get_db
from app.config import get_settings
from app.models.product import Product, ProductCreate, ProductRead, ProductReadWithBrand

settings = get_settings()

router = APIRouter(prefix="/products")


@router.get("/", response_model=List[ProductRead])
def list_products(db: Session = Depends(get_db)):
    stmt = select(Product)
    products = db.exec(stmt).all()
    return products


@router.get("/{product_id}", response_model=ProductReadWithBrand)
def read_product(product_id: int, db: Session = Depends(get_db)):
    product = db.get(Product, product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product


@router.post("/", response_model=ProductRead)
def create_product(product_in: ProductCreate, db: Session = Depends(get_db)):
    product = Product.from_orm(product_in)
    db.add(product)
    db.commit()
    db.refresh(product)
    return product
