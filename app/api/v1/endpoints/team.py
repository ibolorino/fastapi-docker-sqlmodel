from typing import List
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session

from app import crud
from app.api.v1.dependencies import get_db
from app.schemas.team import ITeamCreate, ITeamRead, ITeamReadWithHeroes, ITeamUpdate

router = APIRouter(prefix="/teams")


@router.get("/")
def list_teams(db: Session = Depends(get_db)) -> List[ITeamReadWithHeroes]:
    teams = crud.team.get_all(db=db)
    return teams


@router.get("/{id}")
def retrieve_team(id: UUID, db: Session = Depends(get_db)) -> ITeamReadWithHeroes:
    team = crud.team.get_by_id(db=db, id=id)
    if not team:
        raise HTTPException(status_code=404, detail="Team not found")
    return team


@router.post("/")
def create_team(team_in: ITeamCreate, db: Session = Depends(get_db)) -> ITeamRead:
    team = crud.team.create(db=db, obj_in=team_in)
    return team


@router.put("/{id}")
def update_team(
    *, id: UUID, db: Session = Depends(get_db), team_in: ITeamUpdate
) -> ITeamRead:
    team = crud.team.get_by_id(db=db, id=id)
    if not team:
        raise HTTPException(status_code=404, detail="Team not found")
    team = crud.team.update(db=db, db_obj=team, obj_in=team_in)
    return team


@router.delete("/{id}")
def delete_team(id: UUID, db: Session = Depends(get_db)) -> ITeamRead:
    team = crud.team.get_by_id(db=db, id=id)
    if not team:
        raise HTTPException(status_code=404, detail="Team not found")
    team = crud.team.remove(db, db_obj=team)
    return team
