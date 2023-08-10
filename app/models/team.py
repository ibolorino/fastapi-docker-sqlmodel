from typing import List

from sqlmodel import Field, Relationship, SQLModel

from app.models.base import BaseUUIDModel


class TeamBase(SQLModel):
    name: str = Field(index=True)
    headquarters: str


class Team(BaseUUIDModel, TeamBase, table=True):
    heroes: List["Hero"] = Relationship(  # noqa: F821
        back_populates="team", sa_relationship_kwargs={"lazy": "selctin"}
    )
