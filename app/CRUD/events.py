from sqlalchemy.orm import Session
from app.ORM.models.events import EventModel
from app.core.custom_logger import EventellaLogger
from app.schemas.requests.events import (
    CreateEventRequestSchema, 
    UpdateEventRequestSchema
)
from fastapi import HTTPException
from fastapi.encoders import jsonable_encoder

logger = EventellaLogger(__name__)


def create_event(db: Session, event: CreateEventRequestSchema, user_id: str):
    try:
        event_as_dict = jsonable_encoder(event)
        event = EventModel(**event_as_dict, created_by=user_id)
        db.add(event)
        db.commit()
        db.refresh(event)
        return event
    except Exception as e:
        logger.error(str(e))
        raise HTTPException(
            status_code=400,
            detail=f"{str(e)}"
        )

def get_event(db: Session, event_id: int):
    try:
        event = db.query(EventModel).get(event_id)
        if event == None:
            raise HTTPException(
                status_code=404,
                detail='Not found'
            )
        return event
    except HTTPException as e:
        raise e
    except Exception as e:
        logger.error(str(e))
        raise HTTPException(
            status_code=400,
            detail=f"{str(e)}"
        )

def delete_event(db: Session, event_id: int):
    try:
        event = db.query(EventModel).get(event_id)
        if event == None:
            raise HTTPException(
                status_code=404,
                detail='Not found'
            )
        db.delete(event)
        db.commit()
    except HTTPException as e:
        raise e
    except Exception as e:
        logger.error(str(e))
        raise HTTPException(
            status_code=400,
            detail=f"{str(e)}"
        )

def update_event(db: Session, new_event: UpdateEventRequestSchema, event_id: int):
    try:
        event_as_dict = jsonable_encoder(new_event)
        event = db.query(EventModel).get(event_id)
        if event == None:
            raise HTTPException(
                status_code=404,
                detail='Not found'
            )
        for field in event_as_dict:
            setattr(event, field, event_as_dict[field])
        db.add(event)
        db.commit()
        db.refresh(event)
        return event
    except HTTPException as e:
        raise e        
    except Exception as e:
        logger.error(str(e))
        raise HTTPException(
            status_code=400,
            detail=f"{str(e)}"
        )

def get_events_paginated(db: Session, page: int, limit: int):
    try:
        return db.query(EventModel) \
            .offset(page*limit) \
            .limit(limit) \
            .all()
    except Exception as e:
        logger.error(str(e))
        raise HTTPException(
            status_code=400,
            detail=f"{str(e)}"
        )
