import datetime
from typing import Union
from pydantic import BaseModel

class CreateEventResponseSchema(BaseModel):
    id: int
    name: str
    description: str
    start_date: datetime.datetime
    end_date: datetime.datetime
    location_id: int
    created_by: str
    created_at: datetime.datetime
    updated_at: Union[datetime.datetime, None]

    class Config:
        orm_mode = True

class GetEventResponseSchema(CreateEventResponseSchema, BaseModel):
    pass

class UpdateEventResponseSchema(CreateEventResponseSchema, BaseModel):
    pass

class GetAllEventResponseSchema(CreateEventResponseSchema, BaseModel):
    pass
