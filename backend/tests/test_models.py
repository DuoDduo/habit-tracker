"""
Tests for Habit Model (OOP)
Author: Blessing Oluwapelumi James
Matric No: 92134091

Tests the Habit class methods and streak calculations.
Total: 15 tests
"""

import pytest
from datetime import datetime, timedelta
from app.models.habit import Habit, Completion


class TestHabitCreation:
    """Test habit creation"""
    
    def test_create_habit_basic(self, test_db):
        """Test creating a habit with basic fields"""
        habit = Habit(
            name="Test Habit",
            specification="Test spec",
            periodicity="daily",
            created_at=datetime.now()
        )
        
        test_db.add(habit)
        test_db.commit()
        test_db.refresh(habit)
        
        assert habit.habit_id is not None
        assert habit.name == "Test Habit"
        assert habit.periodicity == "daily"
        assert len(habit.completions) == 0
    
    def test_create_daily_habit(self, test_db):
        """Test creating a daily habit"""
        habit = Habit(
            name="Daily Test",
            specification="Test",
            periodicity="daily",
            created_at=datetime.now()
        )
        
        test_db.add(habit)
        test_db.commit()
        
        assert habit.periodicity == "daily"
    
    def test_create_weekly_habit(self, test_db):
        """Test creating a weekly habit"""
        habit = Habit(
            name="Weekly Test",
            specification="Test",
            periodicity="weekly",
            created_at=datetime.now()
        )
        
        test_db.add(habit)
        test_db.commit()
        
        assert habit.periodicity == "weekly"


class TestStreakCalculation:
    """Test streak calculation methods"""
    
    def test_daily_current_streak(self, test_db):
        """Test current streak for daily habit"""
        habit = Habit(
            name="Daily",
            specification="Test",
            periodicity="daily",
            created_at=datetime.now() - timedelta(days=10)
        )
        test_db.add(habit)
        test_db.commit()
        
        now = datetime.now()
        for i in range(5):
            completion = Completion(
                habit_id=habit.habit_id,
                completion_date=now - timedelta(days=i)
            )
            test_db.add(completion)
        test_db.commit()
        test_db.refresh(habit)
        
        streak = habit.calculate_current_streak(now)
        assert streak == 5
    
    def test_daily_longest_streak(self, test_db):
        """Test longest streak calculation"""
        habit = Habit(
            name="Daily",
            specification="Test",
            periodicity="daily",
            created_at=datetime.now() - timedelta(days=20)
        )
        test_db.add(habit)
        test_db.commit()
        
        now = datetime.now()
        # Create pattern: 7 days, gap, 3 days
        for i in range(7):
            completion = Completion(
                habit_id=habit.habit_id,
                completion_date=now - timedelta(days=i+10)
            )
            test_db.add(completion)
        
        for i in range(3):
            completion = Completion(
                habit_id=habit.habit_id,
                completion_date=now - timedelta(days=i)
            )
            test_db.add(completion)
        
        test_db.commit()
        test_db.refresh(habit)
        
        longest = habit.calculate_longest_streak()
        assert longest == 7
    
    def test_is_broken_daily(self, test_db):
        """Test is_broken for daily habit"""
        habit = Habit(
            name="Daily",
            specification="Test",
            periodicity="daily",
            created_at=datetime.now() - timedelta(days=5)
        )
        test_db.add(habit)
        test_db.commit()
        
        # No completion yesterday = broken
        completion = Completion(
            habit_id=habit.habit_id,
            completion_date=datetime.now() - timedelta(days=2)
        )
        test_db.add(completion)
        test_db.commit()
        test_db.refresh(habit)
        
        assert habit.is_broken(datetime.now()) is True
    
    def test_weekly_current_streak(self, test_db):
        """Test weekly habit streak"""
        habit = Habit(
            name="Weekly",
            specification="Test",
            periodicity="weekly",
            created_at=datetime.now() - timedelta(weeks=5)
        )
        test_db.add(habit)
        test_db.commit()
        
        now = datetime.now()
        for i in range(4):
            completion = Completion(
                habit_id=habit.habit_id,
                completion_date=now - timedelta(weeks=i)
            )
            test_db.add(completion)
        test_db.commit()
        test_db.refresh(habit)
        
        streak = habit.calculate_current_streak(now)
        assert streak >= 3


class TestHabitDeletion:
    """Test habit deletion and CASCADE"""
    
    def test_delete_habit_cascade(self, test_db):
        """Test CASCADE DELETE on completions"""
        habit = Habit(
            name="To Delete",
            specification="Test",
            periodicity="daily",
            created_at=datetime.now()
        )
        test_db.add(habit)
        test_db.commit()
        
        # Add completions
        for i in range(5):
            completion = Completion(
                habit_id=habit.habit_id,
                completion_date=datetime.now() - timedelta(days=i)
            )
            test_db.add(completion)
        test_db.commit()
        
        habit_id = habit.habit_id
        
        # Verify completions exist
        completions_before = test_db.query(Completion).filter(
            Completion.habit_id == habit_id
        ).count()
        assert completions_before == 5
        
        # Delete habit
        test_db.delete(habit)
        test_db.commit()
        
        # Verify completions deleted
        completions_after = test_db.query(Completion).filter(
            Completion.habit_id == habit_id
        ).count()
        assert completions_after == 0