from typing import List
from app.ORM.config import get_db
from app.core.auth import get_auth
from app.core.custom_logger import EventellaLogger
from app.schemas.requests.locations import (
    CreateLocationRequestSchema, 
    UpdateLocationRequestSchema
)
from app.schemas.responses.location import (
    GetAllLocationResponseSchema, 
    GetLocationResponseSchema, 
    UpdateLocationResponseSchema
)
from fastapi import APIRouter, Depends
from ..CRUD import location as locations_crud
from sqlalchemy.orm import Session

logger = EventellaLogger(__name__)
router = APIRouter()

@router.post(
    "",
    summary="Create the new location",
    response_model=GetAllLocationResponseSchema,
    )
async def create_location(
    body: CreateLocationRequestSchema, 
    current_user = Depends(get_auth),
    db: Session = Depends(get_db)
    ):
    return locations_crud.create_location(db, body, current_user.get('sub'))

@router.get(
    "/all",
    summary="Get all locations",
    response_model=List[GetAllLocationResponseSchema]
    )
async def get_locations_paginated(
    page: int = 0,
    limit: int = 50,
    current_user = Depends(get_auth), 
    db: Session = Depends(get_db)
    ):
    return locations_crud.get_locations_paginated(db, page=page, limit=limit)

@router.get(
    "/{location_id}",
    summary="Get the location",
    response_model=GetLocationResponseSchema,
    )
async def get_location(
    location_id: int,
    current_user = Depends(get_auth),  
    db: Session = Depends(get_db)
    ):
    return locations_crud.get_location(db, location_id=location_id)

@router.delete(
    "/{location_id}",
    summary="Delete the location",
    )
async def delete_location(
    location_id: int,
    current_user = Depends(get_auth),  
    db: Session = Depends(get_db)
    ):
    return locations_crud.delete_location(db, location_id=location_id)

@router.put(
    "/{location_id}",
    summary="Update the existing location",
    response_model = UpdateLocationResponseSchema
    )
async def update_location(
    location_id: int,
    body: UpdateLocationRequestSchema, 
    current_user = Depends(get_auth),  
    db: Session = Depends(get_db)
    ):
    return locations_crud.update_location(db, new_location=body, location_id=location_id)
