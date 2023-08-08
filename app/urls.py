from fastapi import APIRouter, FastAPI

from app.api.v1.endpoints import users


def configure_routes(app: FastAPI) -> FastAPI:
    v1 = APIRouter(prefix="/api/v1")
    v1.include_router(users.router, tags=["Users"])
    app.include_router(v1)
    return app
