"""
Database Session Management
Author: Blessing Oluwapelumi James
Matric No: 92134091
"""

# Import create_engine to establish DB connection
# Import event to listen to SQLAlchemy engine events (used for SQLite pragma)
from sqlalchemy import create_engine, event

# Import sessionmaker to create session factory
# Import Session type for type hinting if needed
from sqlalchemy.orm import sessionmaker, Session

# Import Generator for type hinting (if dependency injection was used)
from typing import Generator

# Import contextmanager to safely manage DB session lifecycle
from contextlib import contextmanager

# Import application settings (contains DATABASE_URL, DEBUG mode, etc.)
from app.core.config import settings

# Import Base metadata for table creation
from app.db.base import Base

# Import os for filesystem directory handling
import os


# 1. Get the connection string from settings
# This allows environment-based configuration (.env or defaults)
db_url = settings.DATABASE_URL


# 2. Extract the folder path to ensure it exists
# This handles the 'sqlite:///./data/habits.db' format
if "sqlite" in db_url:
    # Remove the prefix to get the raw relative file path
    # Example: "sqlite:///./data/habits.db" → "./data/habits.db"
    relative_path = db_url.replace("sqlite:///", "")

    # Extract directory name from the database file path
    # Example: "./data/habits.db" → "./data"
    db_dir = os.path.dirname(relative_path)

    # Create directory if it does not exist
    # Prevents runtime failure when SQLite tries to create DB file
    if db_dir and not os.path.exists(db_dir):
        os.makedirs(db_dir)


# 3. Create engine WITHOUT adding the extra fourth slash
# SQLAlchemy engine manages connection pooling and DB communication
engine = create_engine(
    db_url,  # Database connection string
    connect_args={"check_same_thread": False} if "sqlite" in db_url else {},
    # check_same_thread=False is required for SQLite when using multiple threads (e.g., Flask)
    echo=settings.FLASK_DEBUG  # Logs SQL queries in development mode
)


# Enable foreign keys for SQLite
# SQLite does not enforce foreign key constraints by default
@event.listens_for(engine, "connect")
def set_sqlite_pragma(dbapi_conn, connection_record):
    """Enable foreign key constraints for SQLite"""
    
    # Only apply this setting if using SQLite
    if "sqlite" in settings.DATABASE_URL:
        # Obtain raw DB cursor
        cursor = dbapi_conn.cursor()

        # Enable foreign key enforcement
        cursor.execute("PRAGMA foreign_keys=ON")

        # Close cursor after execution
        cursor.close()


# Session factory
# sessionmaker creates new Session objects when called
# autocommit=False → requires explicit commit
# autoflush=False → prevents automatic DB flush before queries
# bind=engine → binds session to this specific engine
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def init_db():
    """Create all tables in the database"""
    
    # Create all tables registered in Base metadata
    # Equivalent to running CREATE TABLE statements
    Base.metadata.create_all(bind=engine)

    # Confirmation message (useful during development)
    print("Database tables created successfully")
 

@contextmanager    
def get_db():
    """
    Dependency to get database session.
    Yields a session and ensures it's closed after use.
    """
    # Create new database session instance
    db = SessionLocal()

    try:
        # Provide session to calling function (e.g., route/service layer)
        yield db

    finally:
        # Prevents connection leaks and ensures clean lifecycle management
        db.close()