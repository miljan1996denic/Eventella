import datetime
from typing import Union
from app.ORM.config import Base
from sqlalchemy import Column, String, Integer, DateTime, ForeignKey, Numeric

class LocationModel(Base):
    __tablename__ = 'location'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    description = Column(String, nullable=True)
    capacity = Column(Integer, nullable=True)
    rent_price = Column(Numeric, nullable=True)
    address = Column(String, nullable=True)
    created_by = Column(String, index=True, nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.now)
    updated_at = Column(DateTime, onupdate=datetime.datetime.now)
