from typing import List, Optional
from uuid import UUID

from app.models.hero import Hero as HeroBase
from app.models.team import TeamBase


class ITeamCreate(TeamBase):
    pass


class ITeamUpdate(TeamBase):
    name: Optional[str]
    headquarters: Optional[str]


class ITeamRead(TeamBase):
    id: UUID


class ITeamReadWithHeroes(ITeamRead):
    heroes: List[HeroBase]
