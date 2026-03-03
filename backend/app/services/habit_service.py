"""
Habit Service - Business Logic Layer
Author: Blessing Oluwapelumi James
Matric No: 92134091
"""

from sqlalchemy.orm import Session
from app.models.habit import Habit, Completion
from app.schemas.habit_schema import HabitCreate
from datetime import datetime
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
            habit = Habit(
                name=name,
                specification=specification,
                periodicity=periodicity,
                created_at=datetime.now()
            )
            
            db.add(habit)
            db.commit()
            db.refresh(habit)
            
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
        habit = db.query(Habit).filter(Habit.habit_id == habit_id).first()
        
        if not habit:
            return False
        
        db.delete(habit)
        db.commit()
        
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
        habit = db.query(Habit).filter(Habit.habit_id == habit_id).first()
        
        if not habit:
            return None
        
        completion = Completion(
            habit_id=habit_id,
            completion_date=timestamp or datetime.now()
        )
        
        db.add(completion)
        db.commit()
        db.refresh(habit)
        
        return habit
    
    @staticmethod
    def update_habit(db: Session, habit_id: int, **kwargs) -> Optional[Habit]:
        habit = db.query(Habit).filter(Habit.habit_id == habit_id).first()
        if not habit:
            return None
        for key, value in kwargs.items():
            setattr(habit, key, value)
        db.commit()
        db.refresh(habit)
        return habit