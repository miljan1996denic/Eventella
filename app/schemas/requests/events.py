import datetime
from pydantic import BaseModel

class CreateEventRequestSchema(BaseModel):
    name: str
    description: str
    start_date: datetime.datetime
    end_date: datetime.datetime
    location_id: int

class UpdateEventRequestSchema(CreateEventRequestSchema, BaseModel):
    pass