from app.models import Team
from app.schemas.team import ITeamCreate, ITeamUpdate

from .base import CRUDBase


class CRUDTeam(CRUDBase[Team, ITeamCreate, ITeamUpdate]):
    pass


team = CRUDTeam(Team)
