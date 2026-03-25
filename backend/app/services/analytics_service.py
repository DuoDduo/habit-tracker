"""
Analytics Service - Functional Programming Approach
Author: Blessing Oluwapelumi James
Matric No: 92134091
This module implements analytics using PURE FUNCTIONAL PROGRAMMING.
All functions are pure: no side effects, same input = same output.

Functional Programming Principles Demonstrated:
- Pure functions
- Immutability
- Higher-order functions (filter, map, max)
- No side effects
"""

# Import List typing for type hints
from typing import List

# Import Habit model to work with habit instances
from app.models.habit import Habit


class AnalyticsService:
    """
    Analytics service using functional programming paradigm.
    All methods are static and pure functions that don't modify input.
    They use Python's built-in functional programming features.
    """
    
    @staticmethod
    def get_habits_by_periodicity(habits: List[Habit], period: str) -> List[Habit]:
        """
        Filter habits by periodicity using functional programming.
        
        Uses built-in filter() with lambda.
        
        Args:
            habits: List of Habit objects
            period: "daily" or "weekly"
            
        Returns:
            Filtered list of habits
        """
        # Apply filter with lambda to select habits where h.periodicity equals given period
        return list(filter(lambda h: h.periodicity == period, habits))
    
    @staticmethod
    def find_longest_streak_all(habits: List[Habit]) -> int:
        """
        Find the longest streak across all habits.
        
        Uses map() to extract streaks, then max() to find highest.
        
        Args:
            habits: List of Habit objects
            
        Returns:
            Longest streak (0 if no habits)
        """
        # Return 0 immediately if no habits are provided
        if not habits:
            return 0
        
        # Map each habit to its longest streak (pure function call)
        streaks = map(lambda h: h.calculate_longest_streak(), habits)
        
        # Return the maximum streak, defaulting to 0 if streaks is empty
        return max(streaks, default=0)
    
    @staticmethod
    def find_longest_streak_for_habit(habit: Habit) -> int:
        """
        Get longest streak for a specific habit.
        
        Args:
            habit: Habit object
            
        Returns:
            Longest streak for this habit
        """
        # Simply call the habit's method to get its longest streak
        return habit.calculate_longest_streak()
    
    @staticmethod
    def get_all_tracked_habits(habits: List[Habit]) -> List[str]:
        """
        Get list of all habit names.
        
        Uses list comprehension (functional style).
        
        Args:
            habits: List of Habit objects
            
        Returns:
            List of habit names
        """
        # Extract habit.name for every habit using list comprehension
        return [h.name for h in habits]
    
    @staticmethod
    def get_struggling_habits(habits: List[Habit], threshold: int = 3) -> List[Habit]:
        """
        Find habits with current streak below threshold.
        
        Uses filter() with lambda to find habits needing attention.
        
        Args:
            habits: List of Habit objects
            threshold: Minimum acceptable streak
            
        Returns:
            Habits with low streaks
        """
        from datetime import datetime  # Import datetime locally for pure function
        
        # Filter habits where current streak (as of now) is below threshold
        return list(filter(
            lambda h: h.calculate_current_streak(datetime.now()) < threshold,
            habits
        ))
    
    @staticmethod
    def count_by_periodicity(habits: List[Habit]) -> dict:
        """
        Count habits by periodicity.
        Uses filter() to separate daily and weekly habits.
        
        Args:
            habits: List of Habit objects
            
        Returns:
            Dict with counts {"daily": x, "weekly": y}
        """
        # Count number of daily habits
        daily = len(list(filter(lambda h: h.periodicity == "daily", habits)))
        
        # Count number of weekly habits
        weekly = len(list(filter(lambda h: h.periodicity == "weekly", habits)))
        
        # Return as dictionary
        return {"daily": daily, "weekly": weekly}