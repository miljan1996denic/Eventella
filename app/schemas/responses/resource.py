import datetime
from typing import Union
from pydantic import BaseModel

class CreateResourceResponseSchema(BaseModel):
    id: int
    name: str
    description: str
    type: str
    quantity: int
    event_id: int
    created_by: str
    created_at: datetime.datetime
    updated_at: Union[datetime.datetime, None]

    class Config:
        orm_mode = True

class GetResourceResponseSchema(CreateResourceResponseSchema, BaseModel):
    pass

class UpdateResourceResponseSchema(CreateResourceResponseSchema, BaseModel):
    pass

class GetAllResourceResponseSchema(CreateResourceResponseSchema, BaseModel):
    pass
