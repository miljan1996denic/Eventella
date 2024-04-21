from gateway.core.log_route import LogRoute
from fastapi import APIRouter
from gateway.routers import (
    gateway
)

api_router = APIRouter(route_class=LogRoute)
api_router.include_router(
    gateway.router,
    tags=["base"]
)