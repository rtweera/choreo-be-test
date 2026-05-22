"""
FastAPI application entry point and configuration.

This module initializes the FastAPI application and registers route handlers.
"""

from typing import Union
from fastapi import FastAPI

from app.routes.router import router as healthRouter

app = FastAPI(
    title="Choreo Backend Test",
    description="A simple backend service for health check monitoring",
    version="1.0.0"
)
app.include_router(healthRouter)

# @app.get("/")
# async def read_root():
#     return {"Hello": "World"}


# @app.get("/items/{item_id}")
# async def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}