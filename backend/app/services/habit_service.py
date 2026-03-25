"""
Habit Service - Business Logic Layer
Author: Blessing Oluwapelumi James
Matric No: 92134091
"""

# Import SQLAlchemy session for database operations
from sqlalchemy.orm import Session

# Import Habit and Completion models for CRUD operations
from app.models.habit import Habit, Completion

# Import Pydantic schema for validation (not strictly used here but available)
from app.schemas.habit_schema import HabitCreate

# Import datetime for timestamps
from datetime import datetime

# Typing hints
from typing import List, Optional


class HabitService:
    """
    Service layer for habit-related business logic.
    Separates business logic from API endpoints.
    """
    
    @staticmethod
    def create_habit(db: Session, name: str, specification: str, periodicity: str) -> Habit:
        """
        Create a new habit.
        
        Args:
            db: Database session
            name: Habit name
            specification: Task description
            periodicity: "daily" or "weekly"
            
        Returns:
            Created Habit instance
        """
        # Instantiate a new Habit object
        habit = Habit(
            name=name,
            specification=specification,
            periodicity=periodicity,
            created_at=datetime.now()  # Set creation timestamp
        )
        
        # Add habit to session for persistence
        db.add(habit)
        
        # Commit transaction to save habit in database
        db.commit()
        
        # Refresh habit to get auto-generated fields like habit_id
        db.refresh(habit)
        
        # Return the created habit
        return habit
        
    @staticmethod
    def get_all_habits(db: Session) -> List[Habit]:
        """
        Get all habits with their completions.
        
        Args:
            db: Database session
            
        Returns:
            List of Habit instances
        """
        # Query all habits from database
        return db.query(Habit).all()
    
    @staticmethod
    def get_habit_by_id(db: Session, habit_id: int) -> Optional[Habit]:
        """
        Get a specific habit by ID.
        
        Args:
            db: Database session
            habit_id: ID of the habit
            
        Returns:
            Habit instance or None if not found
        """
        # Filter habit by primary key and return first match or None
        return db.query(Habit).filter(Habit.habit_id == habit_id).first()
    
    @staticmethod
    def delete_habit(db: Session, habit_id: int) -> bool:
        """
        Delete a habit (CASCADE deletes completions).
        
        Args:
            db: Database session
            habit_id: ID of habit to delete
            
        Returns:
            True if deleted, False if not found
        """
        # Retrieve habit from DB
        habit = db.query(Habit).filter(Habit.habit_id == habit_id).first()
        
        # If habit not found, return False
        if not habit:
            return False
        
        # Delete habit (completions deleted via CASCADE)
        db.delete(habit)
        
        # Commit transaction
        db.commit()
        
        # Return True to indicate successful deletion
        return True
    
    @staticmethod
    def check_off_habit(db: Session, habit_id: int, timestamp: datetime = None) -> Optional[Habit]:
        """
        Record a completion for a habit.
        
        Args:
            db: Database session
            habit_id: ID of habit to check off
            timestamp: Completion time (defaults to now)
            
        Returns:
            Updated Habit instance or None if not found
        """
        # Retrieve habit from database
        habit = db.query(Habit).filter(Habit.habit_id == habit_id).first()
        
        # If habit not found, return None
        if not habit:
            return None
        
        # Create a new Completion record
        completion = Completion(
            habit_id=habit_id,
            completion_date=timestamp or datetime.now()  # Use provided timestamp or current time
        )
        
        # Add completion to session
        db.add(completion)
        
        # Commit transaction to save completion
        db.commit()
        
        # Refresh habit to reflect new completion
        db.refresh(habit)
        
        # Return updated habit
        return habit
    
    @staticmethod
    def update_habit(db: Session, habit_id: int, **kwargs) -> Optional[Habit]:
        """
        Update habit attributes dynamically.
        
        Args:
            db: Database session
            habit_id: ID of habit to update
            **kwargs: Fields to update (name, specification, periodicity)
            
        Returns:
            Updated Habit instance or None if not found
        """
        # Retrieve habit from database
        habit = db.query(Habit).filter(Habit.habit_id == habit_id).first()
        
        # If habit not found, return None
        if not habit:
            return None
        
        # Update all provided fields using setattr
        for key, value in kwargs.items():
            setattr(habit, key, value)
        
        # Commit transaction
        db.commit()
        
        # Refresh habit to reflect updates
        db.refresh(habit)
        
        # Return updated habit
        return habit