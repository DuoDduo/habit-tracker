"""
Habit Model - OOP Domain Model with SQLAlchemy
Author: Blessing Oluwapelumi James
Matric No: 92134091
This module contains the Habit and Completion models using SQLAlchemy ORM.
The Habit class demonstrates OOP principles with encapsulated data and behavior.
"""

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime, timedelta
from typing import List
from app.db.base import Base


class Habit(Base):
    """
    Habit model representing a trackable habit.
    
    This class demonstrates Object-Oriented Programming by encapsulating
    both data (attributes) and behavior (methods) in a single class.
    
    OOP Principles Demonstrated:
    - Encapsulation: Data and methods together
    - Information Hiding: Internal calculation logic hidden
    - Single Responsibility: Manages habit data and streak calculations
    
    Attributes:
        habit_id (int): Unique identifier (Primary Key)
        name (str): Habit name
        specification (str): Detailed description of the task
        periodicity (str): "daily" or "weekly"
        created_at (datetime): When the habit was created
        completions (List[Completion]): Related completion records
    """
    
    __tablename__ = "habits"
    
    # Columns
    habit_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    specification = Column(String(500))
    periodicity = Column(String(20), nullable=False)  # "daily" or "weekly"
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    
    # Relationships with completions (One-to-Many)
    completions = relationship(
        "Completion",
        back_populates="habit",
        cascade="all, delete-orphan",
        lazy="joined"
    )
    
    def __repr__(self):
        """String representation of Habit."""
        return f"<Habit(id={self.habit_id}, name='{self.name}', periodicity='{self.periodicity}')>"
    
    def calculate_current_streak(self, current_date: datetime = None) -> int:
        """
        Calculate the current unbroken streak up to current_date.
        
        This method respects the habit's periodicity:
            - For daily habits: checks for consecutive days
            - For weekly habits: checks for consecutive weeks with at least one completion
            
        Args:
            current_date: Reference date (defaults to now)
            
        Returns:
            Current streak count (days or weeks)
        """
        if current_date is None:
            current_date = datetime.now()
        
        if not self.completions:
            return 0
        
        # Sort completions by date
        sorted_completions = sorted(self.completions, key=lambda c: c.completion_date)
        
        streak = 0
        
        if self.periodicity == "daily":
            check_date = current_date.date()
            
            # Check backwards from current date
            while True:
                has_completion = any(
                    c.completion_date.date() == check_date
                    for c in sorted_completions
                )
                
                if has_completion:
                    streak += 1
                    check_date -= timedelta(days=1)
                else:
                    break
        
        elif self.periodicity == "weekly":
            # Get ISO week number for current date
            current_week = current_date.isocalendar()[1]
            current_year = current_date.isocalendar()[0]
            
            check_week = current_week
            check_year = current_year
            
            while True: 
                # Check if there's any completion in this week
                has_completion = any(
                    c.completion_date.isocalendar()[1] == check_week and
                    c.completion_date.isocalendar()[0] == check_year
                    for c in sorted_completions
                )
                
                if has_completion:
                    streak += 1
                    check_week -= 1
                    if check_week < 1:
                        check_week = 52
                        check_year -= 1
                else:
                    break
        
        return streak
    
    def calculate_longest_streak(self) -> int:
        """
            Calculate the longest streak ever achieved for this habit.
            
            This method finds the maximum consecutive period where the
            habit was completed, respecting the periodicity.
            
            Returns:
                Longest streak count (days or weeks)
                
            Example:
                >>> habit.calculate_longest_streak()
                21  # Best streak was 21 days/weeks
        """
        if not self.completions:
            return 0
        
        max_streak = 0
        current_streak = 0
        
        if self.periodicity == "daily":
            # Get unique dates from completions
            dates = sorted(set(c.completion_date.date() for c in self.completions))
            
            if not dates:
                return 0
            
            current_streak = 1
            max_streak = 1
             # Check for consecutive days
            for i in range(1, len(dates)):
                if dates[i] - dates[i-1] == timedelta(days=1):
                    current_streak += 1
                    max_streak = max(max_streak, current_streak)
                else:
                    current_streak = 1
        
        elif self.periodicity == "weekly":
            # Group completions by week
            weeks = set()
            for c in self.completions:
                week_year = (c.completion_date.isocalendar()[0], 
                           c.completion_date.isocalendar()[1])
                weeks.add(week_year)
            
            weeks = sorted(weeks)
            
            if not weeks:
                return 0
            
            current_streak = 1
            max_streak = 1
            
             # Check for consecutive weeks
            for i in range(1, len(weeks)):
                prev_year, prev_week = weeks[i-1]
                curr_year, curr_week = weeks[i]
                
                # Check if consecutive week
                is_consecutive = False
                if curr_year == prev_year and curr_week == prev_week + 1:
                    is_consecutive = True
                elif curr_year == prev_year + 1 and prev_week == 52 and curr_week == 1:
                    is_consecutive = True
                
                if is_consecutive:
                    current_streak += 1
                    max_streak = max(max_streak, current_streak)
                else:
                    current_streak = 1
        
        return max_streak
    
    def is_broken(self, current_date: datetime = None) -> bool:
        """
        Check if the habit was broken (missed previous period).
        
        A habit is considered broken if:
            - Daily habit: No completion yesterday
            - Weekly habit: No completion last week
        
        Args:
            current_date: Reference date (defaults to now)
            
        Returns:
            True if broken, False otherwise
        """
        if current_date is None:
            current_date = datetime.now()
        
        if not self.completions:
            return True
        
        if self.periodicity == "daily":
             # Check if completed yesterday
            yesterday = (current_date - timedelta(days=1)).date()
            return not any(c.completion_date.date() == yesterday for c in self.completions)
        
        elif self.periodicity == "weekly":
            # Check if completed last week
            last_week = current_date - timedelta(weeks=1)
            last_week_num = last_week.isocalendar()[1]
            last_week_year = last_week.isocalendar()[0]
            
            return not any(
                c.completion_date.isocalendar()[1] == last_week_num and
                c.completion_date.isocalendar()[0] == last_week_year
                for c in self.completions
            )
        
        return False


class Completion(Base):
    """
    Completion model representing when a habit was completed.
    
    This model stores the event log of habit completions,
    which are used for streak calculations.
    
    Attributes:
        completion_id (int): Unique identifier (Primary Key)
        habit_id (int): Foreign Key to habits table
        completion_date (datetime): When the habit was completed
        habit (Habit): Related habit object
    """
    
    __tablename__ = "completions"
    
    # Columns
    completion_id = Column(Integer, primary_key=True, autoincrement=True)
    habit_id = Column(Integer, ForeignKey("habits.habit_id", ondelete="CASCADE"), nullable=False)
    completion_date = Column(DateTime, default=datetime.utcnow, nullable=False)
    
    # Relationships
    habit = relationship("Habit", back_populates="completions")
    
    def __repr__(self):
        """String representation of Completion."""
        return f"<Completion(id={self.completion_id}, habit_id={self.habit_id}, date={self.completion_date})>"