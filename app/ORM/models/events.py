import datetime
from typing import Union
from app.ORM.config import Base
from sqlalchemy import Column, String, Integer, DateTime, ForeignKey

from app.ORM.models.location import LocationModel

class EventModel(Base):
    __tablename__ = 'event'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True, nullable=False)
    description = Column(String, nullable=True)
    start_date = Column(DateTime, nullable=False)
    end_date = Column(DateTime, nullable=False)
    location_id = Column(Integer, ForeignKey(LocationModel.id, ondelete="CASCADE"))
    created_by = Column(String, index=True, nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.now)
    updated_at = Column(DateTime, onupdate=datetime.datetime.now)
