from typing import List
from app.ORM.config import get_db
from app.core.auth import get_auth
from app.core.custom_logger import EventellaLogger
from app.schemas.requests.events import (
    CreateEventRequestSchema, 
    UpdateEventRequestSchema
)
from app.schemas.responses.events import (
    CreateEventResponseSchema,
    GetAllEventResponseSchema, 
    GetEventResponseSchema,
    UpdateEventResponseSchema
)
from fastapi import APIRouter, Depends
from ..CRUD import events as events_crud
from sqlalchemy.orm import Session

logger = EventellaLogger(__name__)
router = APIRouter()

@router.post(
    "",
    summary="Create the new event",
    response_model=CreateEventResponseSchema,
    )
async def create_event(
    body: CreateEventRequestSchema, 
    current_user = Depends(get_auth),  
    db: Session = Depends(get_db)
    ):
    return events_crud.create_event(db, body, current_user.get('sub'))

@router.get(
    "/all",
    summary="Get all events",
    response_model=List[GetAllEventResponseSchema]
    )
async def get_events_paginated(
    page: int = 0,
    limit: int = 50,
    current_user = Depends(get_auth),  
    db: Session = Depends(get_db)
    ):
    return events_crud.get_events_paginated(db, page=page, limit=limit)

@router.get(
    "/{event_id}",
    summary="Get the new event",
    response_model=GetEventResponseSchema,
    )
async def get_event(
    event_id: int,
    current_user = Depends(get_auth),  
    db: Session = Depends(get_db)
    ):
    return events_crud.get_event(db, event_id=event_id)

@router.delete(
    "/{event_id}",
    summary="Delete the event",
    )
async def delete_event(
    event_id: int,
    current_user = Depends(get_auth),  
    db: Session = Depends(get_db)
    ):
    return events_crud.delete_event(db, event_id=event_id)

@router.put(
    "/{event_id}",
    summary="Update the existing event",
    response_model = UpdateEventResponseSchema
    )
async def update_event(
    event_id: int,
    body: UpdateEventRequestSchema, 
    current_user = Depends(get_auth),  
    db: Session = Depends(get_db)
    ):
    return events_crud.update_event(db, new_event=body, event_id=event_id)
