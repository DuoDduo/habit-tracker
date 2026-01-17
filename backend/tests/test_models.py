"""
Tests for Habit Model
Author: Blessing Oluwapelumi James
Matric No: 92134091
"""

import pytest
from datetime import datetime, timedelta
from app.models.habit import Habit, Completion


class TestHabitModel:
    """Tests for Habit class (OOP)"""
    
    def test_habit_creation(self, test_db):
        """Test creating a habit"""
        habit = Habit(
            name="Test Habit",
            specification="Test spec",
            periodicity="daily"
        )
        
        test_db.add(habit)
        test_db.commit()
        
        assert habit.habit_id is not None
        assert habit.name == "Test Habit"
        assert habit.periodicity == "daily"
    
    def test_current_streak_calculation(self, habit_with_streak):
        """Test current streak calculation"""
        streak = habit_with_streak.calculate_current_streak()
        assert streak == 5
    
    def test_longest_streak_calculation(self, test_db):
        """Test longest streak with gaps"""
        habit = Habit(name="Test", specification="Test", periodicity="daily")
        test_db.add(habit)
        test_db.commit()
        
        now = datetime.now()
        
        # Create pattern: 3 days, gap, 5 days
        dates = [
            now - timedelta(days=10),
            now - timedelta(days=9),
            now - timedelta(days=8),
            # Gap
            now - timedelta(days=5),
            now - timedelta(days=4),
            now - timedelta(days=3),
            now - timedelta(days=2),
            now - timedelta(days=1)
        ]
        
        for date in dates:
            completion = Completion(habit_id=habit.habit_id, completion_date=date)
            test_db.add(completion)
        
        test_db.commit()
        test_db.refresh(habit)
        
        longest = habit.calculate_longest_streak()
        assert longest == 5
    
    def test_is_broken(self, test_db):
        """Test broken status"""
        habit = Habit(name="Test", specification="Test", periodicity="daily")
        test_db.add(habit)
        test_db.commit()
        
        # Habit with no completions should be broken
        assert habit.is_broken() is True
        
        # Add completion for yesterday
        yesterday = datetime.now() - timedelta(days=1)
        completion = Completion(habit_id=habit.habit_id, completion_date=yesterday)
        test_db.add(completion)
        test_db.commit()
        test_db.refresh(habit)
        
        # Should not be broken
        assert habit.is_broken() is False