from typing import List

from fastapi import APIRouter, Depends
from sqlmodel import Session, select

from app.api.v1.dependencies import get_db
from app.models.team import Team
from app.schemas.team import ITeamCreate, ITeamRead

router = APIRouter(prefix="/teams")


@router.get("/")
def list_teams(db: Session = Depends(get_db)) -> List[ITeamRead]:
    stmt = select(Team)
    teams = db.exec(stmt).all()
    return teams


@router.post("/")
def create_team(team_in: ITeamCreate, db: Session = Depends(get_db)) -> ITeamRead:
    team_obj = Team.from_orm(team_in)
    db.add(team_obj)
    db.commit()
    db.refresh(team_obj)
    return team_obj
