from typing import Optional
from uuid import UUID

from sqlmodel import Field, Relationship, SQLModel

from app.models.base import BaseUUIDModel


class HeroBase(SQLModel):
    name: str = Field(index=True)
    age: Optional[int]
    team_id: Optional[UUID] = Field(default=None, foreign_key="team.id")


class Hero(BaseUUIDModel, HeroBase, table=True):
    team: "Team" = Relationship(  # noqa: F821
        back_populates="heroes",
        sa_relationship={"lazy": "joined", "primaryjoin": "Hero.team_id==Team.id"},
    )
