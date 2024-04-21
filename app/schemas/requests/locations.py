from pydantic import BaseModel

class CreateLocationRequestSchema(BaseModel):
    name: str
    description: str
    capacity: int
    rent_price: float
    address: str

class UpdateLocationRequestSchema(CreateLocationRequestSchema, BaseModel):
    pass
