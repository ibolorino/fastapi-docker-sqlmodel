from fastapi import FastAPI

from .urls import configure_routes

app = FastAPI()

app = configure_routes(app=app)
