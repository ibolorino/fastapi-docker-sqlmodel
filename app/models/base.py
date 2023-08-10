import uuid
from datetime import datetime
from typing import Optional

from sqlalchemy.orm import declared_attr
from sqlmodel import Field
from sqlmodel import SQLModel as _SQLModel


class SQLModel(_SQLModel):
    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()


class BaseModel(SQLModel):
    created_at: Optional[datetime] = Field(default_factory=datetime.utcnow)
    updated_at: Optional[datetime] = Field(default_factory=datetime.utcnow)


class BaseUUIDModel(BaseModel):
    id: uuid.UUID = Field(
        default_factory=uuid.uuid4, primary_key=True, index=True, nullable=False
    )


class BaseIntModel(BaseModel):
    id: int = Field(default=None, primary_key=True, index=True, nullable=False)
