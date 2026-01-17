"""
Tests for Services Layer
Author: Blessing Oluwapelumi James
Matric No: 92134091
"""

import pytest
from app.services.habit_service import HabitService
from app.services.analytics_service import AnalyticsService
from app.schemas.habit_schema import HabitCreate


class TestHabitService:
    """Tests for HabitService"""
    
    def test_create_habit(self, test_db):
        """Test creating habit via service"""
        habit_data = HabitCreate(
            name="New Habit",
            specification="New spec",
            periodicity="daily"
        )
        
        habit = HabitService.create_habit(test_db, habit_data)
        
        assert habit.habit_id is not None
        assert habit.name == "New Habit"
    
    def test_get_all_habits(self, test_db, sample_habit):
        """Test getting all habits"""
        habits = HabitService.get_all_habits(test_db)
        
        assert len(habits) >= 1
        assert any(h.habit_id == sample_habit.habit_id for h in habits)
    
    def test_check_off_habit(self, test_db, sample_habit):
        """Test checking off a habit"""
        updated = HabitService.check_off_habit(test_db, sample_habit.habit_id)
        
        assert updated is not None
        assert len(updated.completions) == 1


class TestAnalyticsService:
    """Tests for AnalyticsService (Functional Programming)"""
    
    def test_filter_by_periodicity(self, test_db):
        """Test filtering habits by periodicity"""
        # Create mix of habits
        daily = Habit(name="Daily", specification="", periodicity="daily")
        weekly = Habit(name="Weekly", specification="", periodicity="weekly")
        
        test_db.add_all([daily, weekly])
        test_db.commit()
        
        habits = test_db.query(Habit).all()
        
        daily_habits = AnalyticsService.get_habits_by_periodicity(habits, "daily")
        weekly_habits = AnalyticsService.get_habits_by_periodicity(habits, "weekly")
        
        assert len(daily_habits) >= 1
        assert len(weekly_habits) >= 1
        assert all(h.periodicity == "daily" for h in daily_habits)
    
    def test_longest_streak_all(self, test_db, habit_with_streak):
        """Test finding longest streak across all habits"""
        habits = test_db.query(Habit).all()
        
        longest = AnalyticsService.find_longest_streak_all(habits)
        
        assert longest >= 5
    
    def test_get_tracked_habits(self, test_db, sample_habit):
        """Test getting habit names"""
        habits = test_db.query(Habit).all()
        
        names = AnalyticsService.get_all_tracked_habits(habits)
        
        assert "Test Habit" in names