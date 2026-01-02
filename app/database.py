"""
Database configuration file
- Creates PostgreSQL connection
- Provides DB session dependency
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# PostgreSQL connection string
DATABASE_URL = "postgresql://postgres:postgres@db:5432/fastapi_db"

# Create SQLAlchemy engine
engine = create_engine(DATABASE_URL)

# Session factory
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# Base class for models
Base = declarative_base()
