"""
Main application file
- Defines API routes
- Injects DB dependencies
"""

from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from .database import SessionLocal, engine
from . import models, schemas, crud

# Create database tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="FastAPI PostgreSQL CRUD")

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/items/", response_model=schemas.Item)
def create_item(item: schemas.ItemCreate, db: Session = Depends(get_db)):
    """Create item endpoint"""
    return crud.create_item(db, item)

@app.get("/items/", response_model=list[schemas.Item])
def read_items(db: Session = Depends(get_db)):
    """List all items"""
    return crud.get_items(db)

@app.get("/items/{item_id}", response_model=schemas.Item)
def read_item(item_id: int, db: Session = Depends(get_db)):
    """Get item by ID"""
    item = crud.get_item(db, item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

@app.delete("/items/{item_id}", response_model=schemas.Item)
def delete_item(item_id: int, db: Session = Depends(get_db)):
    """Delete item"""
    item = crud.delete_item(db, item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item
