from typing import List

from fastapi import APIRouter, Depends
from sqlmodel import Session, select

from app.api.v1.dependencies import get_db
from app.config import get_settings
from app.models.brand import Brand, BrandCreate, BrandRead

settings = get_settings()

router = APIRouter(prefix="/brands")


@router.get("/", response_model=List[BrandRead])
def list_Brands(db: Session = Depends(get_db)):
    stmt = select(Brand)
    brands = db.exec(stmt).all()
    return brands


@router.post("/", response_model=BrandRead)
def create_user(brand_in: BrandCreate, db: Session = Depends(get_db)):
    brand = Brand.from_orm(brand_in)
    db.add(brand)
    db.commit()
    db.refresh(brand)
    return brand
