import datetime
from typing import Union
from pydantic import BaseModel

class CreateLocationResponseSchema(BaseModel):
    id: int
    name: str
    description: str
    capacity: int
    rent_price: float
    address: str
    created_by: str
    created_at: datetime.datetime
    updated_at: Union[datetime.datetime, None]

    class Config:
        orm_mode = True

class GetLocationResponseSchema(CreateLocationResponseSchema, BaseModel):
    pass

class UpdateLocationResponseSchema(CreateLocationResponseSchema, BaseModel):
    pass

class GetAllLocationResponseSchema(CreateLocationResponseSchema, BaseModel):
    pass
