"""
Analytics Service - Functional Programming Approach
Author: Blessing Oluwapelumi James
Matric No: 92134091

All functions are PURE - no side effects, same input = same output
"""

from typing import List
from app.models.habit import Habit


class AnalyticsService:
    """
    Analytics service using functional programming paradigm.
    All methods are static and pure functions.
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
        if not habits:
            return 0
        
        streaks = map(lambda h: h.calculate_longest_streak(), habits)
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
        return [h.name for h in habits]
    
    @staticmethod
    def get_struggling_habits(habits: List[Habit], threshold: int = 3) -> List[Habit]:
        """
        Find habits with current streak below threshold.
        
        Uses filter() with lambda.
        
        Args:
            habits: List of Habit objects
            threshold: Minimum acceptable streak
            
        Returns:
            Habits with low streaks
        """
        from datetime import datetime
        return list(filter(
            lambda h: h.calculate_current_streak(datetime.now()) < threshold,
            habits
        ))
    
    @staticmethod
    def count_by_periodicity(habits: List[Habit]) -> dict:
        """
        Count habits by periodicity.
        
        Args:
            habits: List of Habit objects
            
        Returns:
            Dict with counts {"daily": x, "weekly": y}
        """
        daily = len(list(filter(lambda h: h.periodicity == "daily", habits)))
        weekly = len(list(filter(lambda h: h.periodicity == "weekly", habits)))
        
        return {"daily": daily, "weekly": weekly}