from fastapi import APIRouter, FastAPI

from app.api.v1.endpoints import team, users


def configure_routes(app: FastAPI) -> FastAPI:
    v1 = APIRouter(prefix="/api/v1")
    v1.include_router(users.router, tags=["Users"])
    v1.include_router(team.router, tags=["Teams"])
    app.include_router(v1)
    return app
