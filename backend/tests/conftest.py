"""
Pytest Configuration and Fixtures
Author: Blessing Oluwapelumi James
Matric No: 92134091
"""

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.db.base import Base
from app.models.habit import Habit, Completion
from app.main import create_app
from datetime import datetime, timedelta


@pytest.fixture(scope="function")
def test_db():
    """Create a test database for each test function"""
    engine = create_engine("sqlite:///:memory:")
    Base.metadata.create_all(engine)
    
    SessionLocal = sessionmaker(bind=engine)
    db = SessionLocal()
    
    yield db
    
    db.close()
    Base.metadata.drop_all(engine)


@pytest.fixture(scope="function")
def sample_habit(test_db):
    """Create a sample habit for testing"""
    habit = Habit(
        name="Test Habit",
        specification="Test specification",
        periodicity="daily",
        created_at=datetime.now()
    )
    
    test_db.add(habit)
    test_db.commit()
    test_db.refresh(habit)
    
    return habit


@pytest.fixture(scope="function")
def habit_with_streak(test_db):
    """Create a habit with a 5-day streak"""
    habit = Habit(
        name="Streak Habit",
        specification="Has a streak",
        periodicity="daily",
        created_at=datetime.now() - timedelta(days=10)
    )
    
    test_db.add(habit)
    test_db.commit()
    
    # Add 5 consecutive days
    now = datetime.now()
    for i in range(5):
        completion = Completion(
            habit_id=habit.habit_id,
            completion_date=now - timedelta(days=i)
        )
        test_db.add(completion)
    
    test_db.commit()
    test_db.refresh(habit)
    
    return habit


@pytest.fixture(scope="module")
def test_client():
    """Create a test client for API testing"""
    app = create_app()
    app.config["TESTING"] = True
    
    with app.test_client() as client:
        yield client