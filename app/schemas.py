"""
Pydantic schemas
- Used for request validation
- Used for response serialization
"""

from pydantic import BaseModel

# Shared fields
class ItemBase(BaseModel):
    name: str
    description: str | None = None

# Request schema
class ItemCreate(ItemBase):
    pass

# Response schema
class Item(ItemBase):
    id: int

    class Config:
        from_attributes = True
