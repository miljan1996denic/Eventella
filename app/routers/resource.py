from typing import List
from app.ORM.config import get_db
from app.core.auth import get_auth
from app.core.custom_logger import EventellaLogger
from app.schemas.requests.resources import (
    CreateResourceRequestSchema, 
    UpdateResourceRequestSchema
)
from app.schemas.responses.resource import (
    GetAllResourceResponseSchema, 
    GetResourceResponseSchema, 
    UpdateResourceResponseSchema
)
from fastapi import APIRouter, Depends
from ..CRUD import resource as resources_crud
from sqlalchemy.orm import Session

logger = EventellaLogger(__name__)
router = APIRouter()

@router.post(
    "",
    summary="Create the new resource",
    response_model=GetAllResourceResponseSchema,
    )
async def create_resource(
    body: CreateResourceRequestSchema, 
    current_user = Depends(get_auth),
    db: Session = Depends(get_db)
    ):
    return resources_crud.create_resource(db, body, current_user.get('sub'))

@router.get(
    "/all",
    summary="Get all resources",
    response_model=List[GetAllResourceResponseSchema]
    )
async def get_resources_paginated(
    page: int = 0,
    limit: int = 50,
    current_user = Depends(get_auth), 
    db: Session = Depends(get_db)
    ):
    return resources_crud.get_resources_paginated(db, page=page, limit=limit)

@router.get(
    "/{resource_id}",
    summary="Get the resource",
    response_model=GetResourceResponseSchema,
    )
async def get_resource(
    resource_id: int,
    current_user = Depends(get_auth),
    db: Session = Depends(get_db)
    ):
    return resources_crud.get_resource(db, resource_id=resource_id)

@router.delete(
    "/{resource_id}",
    summary="Delete the resource",
    )
async def delete_resource(
    resource_id: int,
    current_user = Depends(get_auth),
    db: Session = Depends(get_db)
    ):
    return resources_crud.delete_resource(db, resource_id=resource_id)

@router.put(
    "/{resource_id}",
    summary="Update the existing resource",
    response_model = UpdateResourceResponseSchema
    )
async def update_resource(
    resource_id: int,
    body: UpdateResourceRequestSchema, 
    current_user = Depends(get_auth),
    db: Session = Depends(get_db)
    ):
    return resources_crud.update_resource(db, new_resource=body, resource_id=resource_id)
