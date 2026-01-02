"""
CRUD operations
- All database logic lives here
"""

from sqlalchemy.orm import Session
from . import models, schemas

def get_items(db: Session):
    """Return all items"""
    return db.query(models.Item).all()

def get_item(db: Session, item_id: int):
    """Return one item by ID"""
    return db.query(models.Item).filter(models.Item.id == item_id).first()

def create_item(db: Session, item: schemas.ItemCreate):
    """Create a new item"""
    db_item = models.Item(**item.model_dump())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def delete_item(db: Session, item_id: int):
    """Delete an item"""
    item = get_item(db, item_id)
    if item:
        db.delete(item)
        db.commit()
    return item
