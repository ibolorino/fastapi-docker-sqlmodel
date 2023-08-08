from typing import List

from fastapi import APIRouter, Depends
from sqlmodel import Session, select

from app.api.v1.dependencies import get_db
from app.api.v1.security import get_password_hash
from app.config import get_settings
from app.models.user import User, UserCreate, UserRead

settings = get_settings()

router = APIRouter(prefix="/users")


@router.get("/", response_model=List[UserRead])
def list_users(db: Session = Depends(get_db)):
    stmt = select(User)
    users = db.exec(stmt).all()
    return users


@router.post("/", response_model=UserRead)
def create_user(user_in: UserCreate, db: Session = Depends(get_db)):
    user_in.password = get_password_hash(user_in.password, user_in.confirm_password)
    user = User.from_orm(user_in)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user
