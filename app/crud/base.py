from typing import Generic, List, TypeVar, Union
from uuid import UUID

from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from sqlmodel import Session, SQLModel, select

ModelType = TypeVar("ModelType", bound=SQLModel)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)


class CRUDBase(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    def __init__(self, model: type[ModelType]):
        self.model = model

    def get_by_id(self, db: Session, id: Union[UUID, int]) -> Union[ModelType, None]:
        query = select(self.model).where(self.model.id == id)
        response = db.exec(query).first()
        return response

    def get_all(self, db: Session) -> Union[List[ModelType], None]:
        query = select(self.model)
        response = db.exec(query).all()
        return response

    def create(self, db: Session, obj_in: CreateSchemaType) -> ModelType:
        db_obj = self.model.from_orm(obj_in)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def update(
        self, db: Session, db_obj: ModelType, obj_in=UpdateSchemaType
    ) -> ModelType:
        obj_data = jsonable_encoder(db_obj)
        update_data = obj_in.dict(exclude_unset=True)
        for field in obj_data:
            if field in update_data:
                setattr(db_obj, field, update_data[field])
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def remove(self, db: Session, db_obj: ModelType) -> ModelType:
        db.delete(db_obj)
        db.commit()
        return db_obj
