from typing import Generator

# from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer, OAuth2PasswordBearer

# from app import crud
from app.config import get_settings
from app.database.session import local_session

# from jose import jwt
# from sqlmodel import Session


# from app.models.token import TokenPayload
# from app.models.user import User

settings = get_settings()
reusable_oauth2 = OAuth2PasswordBearer(tokenUrl=f"{settings.API_V1_STR}/auth/login")
token_auth_scheme = HTTPBearer()


def get_db() -> Generator:
    try:
        db = local_session
        yield db
    finally:
        db.close()


# def get_current_user(
#     db: Session = Depends(get_db), token: str = Depends(reusable_oauth2)
# ) -> User:
#     try:
#         payload = jwt.decode(
#             token, settings.SECRET_KEY, algorithms=[settings.JWT_ALGORITHM]
#         )
#         token_data = TokenPayload(**payload)
#     except Exception:
#         raise HTTPException(
#             status_code=403, detail="Não foi possível validar as credenciais"
#         )
#     user = crud.user.get(db, token_data.sub)
#     if not user:
#         raise HTTPException(status_code=404, detail="Usuário não encontrado")
#     return user


# def get_current_active_user(current_user: User = Depends(get_current_user)) -> User:
#     if not crud.user.is_active(current_user):
#         raise HTTPException(status_code=400, detail="Usuário inativo")
#     return current_user


# def get_current_active_superuser(
#     current_user: User = Depends(get_current_active_user),
# ) -> User:
#     if not crud.user.is_active(current_user):
#         raise HTTPException(
#             status_code=400, detail="Usuário não tem privilégios suficientes"
#         )
#     return current_user
