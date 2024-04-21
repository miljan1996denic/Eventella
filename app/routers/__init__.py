from app.core.log_route import LogRoute
from fastapi import APIRouter
from app.routers import (
    events, 
    location,
    resource
)

api_router = APIRouter(route_class=LogRoute)
api_router.include_router(
    events.router,
    prefix="/event",
    tags=["event"]
)
api_router.include_router(
    location.router,
    prefix="/location",
    tags=["location"]
)
api_router.include_router(
    resource.router,
    prefix="/resource",
    tags=["resource"]
)