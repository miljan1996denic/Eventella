from sqlalchemy.orm import Session
from app.ORM.models.resource import ResourceModel
from app.core.custom_logger import EventellaLogger
from app.schemas.requests.resources import (
    CreateResourceRequestSchema, 
    UpdateResourceRequestSchema
)
from fastapi import HTTPException
from fastapi.encoders import jsonable_encoder

logger = EventellaLogger(__name__)


def create_resource(db: Session, resource: CreateResourceRequestSchema, user_id: str):
    try:
        resource_as_dict = jsonable_encoder(resource)
        resource = ResourceModel(**resource_as_dict, created_by=user_id)
        db.add(resource)
        db.commit()
        db.refresh(resource)
        return resource
    except Exception as e:
        logger.error(str(e))
        raise HTTPException(
            status_code=400,
            detail=f"{str(e)}"
        )

def get_resource(db: Session, resource_id: int):
    try:
        resource = db.query(ResourceModel).get(resource_id)
        if resource == None:
            raise HTTPException(
                status_code=404,
                detail='Not found'
            )
        return resource
    except HTTPException as e:
        raise e
    except Exception as e:
        logger.error(str(e))
        raise HTTPException(
            status_code=400,
            detail=f"{str(e)}"
        )

def delete_resource(db: Session, resource_id: int):
    try:
        resource = db.query(ResourceModel).get(resource_id)
        if resource == None:
            raise HTTPException(
                status_code=404,
                detail='Not found'
            )
        db.delete(resource)
        db.commit()
    except HTTPException as e:
        raise e
    except Exception as e:
        logger.error(str(e))
        raise HTTPException(
            status_code=400,
            detail=f"{str(e)}"
        )

def update_resource(db: Session, new_resource: UpdateResourceRequestSchema, resource_id: int):
    try:
        resource_as_dict = jsonable_encoder(new_resource)
        resource = db.query(ResourceModel).get(resource_id)
        if resource == None:
            raise HTTPException(
                status_code=404,
                detail='Not found'
            )
        for field in resource_as_dict:
            setattr(resource, field, resource_as_dict[field])
        db.add(resource)
        db.commit()
        db.refresh(resource)
        return resource
    except HTTPException as e:
        raise e        
    except Exception as e:
        logger.error(str(e))
        raise HTTPException(
            status_code=400,
            detail=f"{str(e)}"
        )

def get_resources_paginated(db: Session, page: int, limit: int):
    try:
        return db.query(ResourceModel).offset(page*limit).limit(limit).all()
    except Exception as e:
        logger.error(str(e))
        raise HTTPException(
            status_code=400,
            detail=f"{str(e)}"
        )
