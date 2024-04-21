from sqlalchemy.orm import Session
from app.ORM.models.location import LocationModel
from app.core.custom_logger import EventellaLogger
from app.schemas.requests.locations import (
    CreateLocationRequestSchema, 
    UpdateLocationRequestSchema
)
from fastapi import HTTPException
from fastapi.encoders import jsonable_encoder

logger = EventellaLogger(__name__)


def create_location(db: Session, location: CreateLocationRequestSchema, user_id: str):
    try:
        location_as_dict = jsonable_encoder(location)
        location = LocationModel(**location_as_dict, created_by=user_id)
        db.add(location)
        db.commit()
        db.refresh(location)
        return location
    except Exception as e:
        logger.error(str(e))
        raise HTTPException(
            status_code=400,
            detail=f"{str(e)}"
        )

def get_location(db: Session, location_id: int):
    try:
        location = db.query(LocationModel).get(location_id)
        if location == None:
            raise HTTPException(
                status_code=404,
                detail='Not found'
            )
        return location
    except HTTPException as e:
        raise e
    except Exception as e:
        logger.error(str(e))
        raise HTTPException(
            status_code=400,
            detail=f"{str(e)}"
        )

def delete_location(db: Session, location_id: int):
    try:
        location = db.query(LocationModel).get(location_id)
        if location == None:
            raise HTTPException(
                status_code=404,
                detail='Not found'
            )
        db.delete(location)
        db.commit()
    except HTTPException as e:
        raise e
    except Exception as e:
        logger.error(str(e))
        raise HTTPException(
            status_code=400,
            detail=f"{str(e)}"
        )

def update_location(db: Session, new_location: UpdateLocationRequestSchema, location_id: int):
    try:
        location_as_dict = jsonable_encoder(new_location)
        location = db.query(LocationModel).get(location_id)
        if location == None:
            raise HTTPException(
                status_code=404,
                detail='Not found'
            )
        for field in location_as_dict:
            setattr(location, field, location_as_dict[field])
        db.add(location)
        db.commit()
        db.refresh(location)
        return location
    except HTTPException as e:
        raise e        
    except Exception as e:
        logger.error(str(e))
        raise HTTPException(
            status_code=400,
            detail=f"{str(e)}"
        )

def get_locations_paginated(db: Session, page: int, limit: int):
    try:
        return db.query(LocationModel).offset(page*limit).limit(limit).all()
    except Exception as e:
        logger.error(str(e))
        raise HTTPException(
            status_code=400,
            detail=f"{str(e)}"
        )
