from pydantic import BaseModel

class CreateResourceRequestSchema(BaseModel):
    name: str
    description: str
    type: str
    quantity: int
    event_id: int

class UpdateResourceRequestSchema(CreateResourceRequestSchema, BaseModel):
    pass
