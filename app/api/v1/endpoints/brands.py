from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select

from app.api.v1.dependencies import get_db
from app.config import get_settings
from app.models.brand import Brand, BrandCreate, BrandRead, BrandReadWithProducts

settings = get_settings()

router = APIRouter(prefix="/brands")


@router.get("/", response_model=List[BrandRead])
def list_brands(db: Session = Depends(get_db)):
    stmt = select(Brand)
    brands = db.exec(stmt).all()
    return brands


@router.get("/{brand_id}", response_model=BrandReadWithProducts)
def read_brand(brand_id: int, db: Session = Depends(get_db)):
    brand = db.get(Brand, brand_id)
    if not brand:
        raise HTTPException(status_code=404, detail="Brand not found")
    return brand


@router.post("/", response_model=BrandRead)
def create_product(brand_in: BrandCreate, db: Session = Depends(get_db)):
    brand = Brand.from_orm(brand_in)
    db.add(brand)
    db.commit()
    db.refresh(brand)
    return brand
