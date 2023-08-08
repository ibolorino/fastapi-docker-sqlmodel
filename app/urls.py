from fastapi import APIRouter, FastAPI

from app.api.v1.endpoints import products, users


def configure_routes(app: FastAPI) -> FastAPI:
    v1 = APIRouter(prefix="/api/v1")
    v1.include_router(users.router, tags=["Users"])
    v1.include_router(products.router, tags=["Products"])
    app.include_router(v1)
    return app
