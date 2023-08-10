from typing import Optional
from uuid import UUID

from pydantic import validator

from app.models.hero import Hero as HeroBase
from app.models.team import TeamBase


class IHeroCreate(HeroBase):
    @validator("age", pre=True, check_fields=False, always=True)
    def validate_age(cls, value, values, **kwargs) -> int:
        if value < 0:
            raise ValueError("Invalid age")
        return value


class IHeroUpdate(HeroBase):
    name: Optional[str]


class IHeroRead(HeroBase):
    id: UUID


class IHeroReadWithTeam(IHeroRead):
    team: Optional[TeamBase]
