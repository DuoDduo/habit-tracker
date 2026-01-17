"""
Database Session Management
Author: Blessing Oluwapelumi James
Matric No: 92134091
"""

from sqlalchemy import create_engine, event
from sqlalchemy.orm import sessionmaker, Session
from app.core.config import settings
from app.db.base import Base
import os


# 1. Get the connection string from settings
db_url = settings.DATABASE_URL

# 2. Extract the folder path to ensure it exists
# This handles the 'sqlite:///./data/habits.db' format
if "sqlite" in db_url:
    # Remove the prefix to get the raw path
    relative_path = db_url.replace("sqlite:///", "")
    # Ensure the directory (e.g., './data') exists
    db_dir = os.path.dirname(relative_path)
    if db_dir and not os.path.exists(db_dir):
        os.makedirs(db_dir)

# 3. Create engine WITHOUT adding the extra fourth slash
engine = create_engine(
    db_url, 
    connect_args={"check_same_thread": False} if "sqlite" in db_url else {},
    echo=settings.FLASK_DEBUG
)


# Enable foreign keys for SQLite
@event.listens_for(engine, "connect")
def set_sqlite_pragma(dbapi_conn, connection_record):
    """Enable foreign key constraints for SQLite"""
    if "sqlite" in settings.DATABASE_URL:
        cursor = dbapi_conn.cursor()
        cursor.execute("PRAGMA foreign_keys=ON")
        cursor.close()


# Session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def init_db():
    """Create all tables in the database"""
    Base.metadata.create_all(bind=engine)
    print("✅ Database tables created successfully")


def get_db() -> Session:
    """
    Dependency to get database session.
    Yields a session and ensures it's closed after use.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()