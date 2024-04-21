import datetime
from app.ORM.config import Base
from sqlalchemy import Column, String, Integer, DateTime, ForeignKey

from app.ORM.models.events import EventModel

class ResourceModel(Base):
    __tablename__ = 'resource'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    description = Column(String, nullable=True)
    type = Column(String, nullable=False)
    quantity = Column(Integer, default=0, nullable=False)
    event_id = Column(Integer, ForeignKey(EventModel.id, ondelete="CASCADE"))
    created_by = Column(String, index=True, nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.now)
    updated_at = Column(DateTime, onupdate=datetime.datetime.now)
