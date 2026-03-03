"""
Tests for Service Layer
Author: Blessing Oluwapelumi James
Matric No: 92134091

Tests business logic in HabitService and AnalyticsService.
Total: 15 tests
"""

import pytest
from app.services.habit_service import HabitService
from app.services.analytics_service import AnalyticsService
from app.models.habit import Habit, Completion
from datetime import datetime, timedelta


class TestHabitService:
    """Test HabitService methods"""
    
    def test_create_habit(self, test_db):
        """Test creating habit via service"""
        habit = HabitService.create_habit(
            db=test_db,
            name="Service Test",
            specification="Created via service",
            periodicity="daily"
        )
        
        assert habit.habit_id is not None
        assert habit.name == "Service Test"
    
    def test_get_all_habits(self, test_db, sample_habit):
        """Test getting all habits"""
        habits = HabitService.get_all_habits(test_db)
        
        assert len(habits) >= 1
        assert any(h.habit_id == sample_habit.habit_id for h in habits)
    
    def test_get_habit_by_id(self, test_db, sample_habit):
        """Test getting habit by ID"""
        habit = HabitService.get_habit_by_id(test_db, sample_habit.habit_id)
        
        assert habit is not None
        assert habit.habit_id == sample_habit.habit_id
    
    def test_delete_habit(self, test_db, sample_habit):
        """Test deleting habit"""
        habit_id = sample_habit.habit_id
        success = HabitService.delete_habit(test_db, habit_id)
        
        assert success is True
        assert HabitService.get_habit_by_id(test_db, habit_id) is None
    
    def test_check_off_habit(self, test_db, sample_habit):
        """Test checking off habit"""
        updated = HabitService.check_off_habit(test_db, sample_habit.habit_id)
        
        assert updated is not None
        assert len(updated.completions) == 1


class TestAnalyticsService:
    """Test AnalyticsService (Functional Programming)"""
    
    def test_filter_by_periodicity_daily(self, test_db):
        """Test filtering daily habits"""
        daily1 = Habit(name="Daily 1", specification="", periodicity="daily", created_at=datetime.now())
        daily2 = Habit(name="Daily 2", specification="", periodicity="daily", created_at=datetime.now())
        weekly = Habit(name="Weekly", specification="", periodicity="weekly", created_at=datetime.now())
        
        test_db.add_all([daily1, daily2, weekly])
        test_db.commit()
        
        all_habits = test_db.query(Habit).all()
        daily_habits = AnalyticsService.get_habits_by_periodicity(all_habits, "daily")
        
        assert len(daily_habits) == 2
        assert all(h.periodicity == "daily" for h in daily_habits)
    
    def test_filter_by_periodicity_weekly(self, test_db):
        """Test filtering weekly habits"""
        daily = Habit(name="Daily", specification="", periodicity="daily", created_at=datetime.now())
        weekly = Habit(name="Weekly", specification="", periodicity="weekly", created_at=datetime.now())
        
        test_db.add_all([daily, weekly])
        test_db.commit()
        
        all_habits = test_db.query(Habit).all()
        weekly_habits = AnalyticsService.get_habits_by_periodicity(all_habits, "weekly")
        
        assert len(weekly_habits) == 1
        assert weekly_habits[0].periodicity == "weekly"
    
    def test_longest_streak_all(self, test_db):
        """Test finding longest streak across all habits"""
        habit1 = Habit(name="H1", specification="", periodicity="daily", created_at=datetime.now())
        habit2 = Habit(name="H2", specification="", periodicity="daily", created_at=datetime.now())
        
        test_db.add_all([habit1, habit2])
        test_db.commit()
        
        now = datetime.now()
        
        # Habit 1: 5-day streak
        for i in range(5):
            completion = Completion(habit_id=habit1.habit_id, completion_date=now - timedelta(days=i+5))
            test_db.add(completion)
        
        # Habit 2: 8-day streak (longest)
        for i in range(8):
            completion = Completion(habit_id=habit2.habit_id, completion_date=now - timedelta(days=i))
            test_db.add(completion)
        
        test_db.commit()
        
        all_habits = test_db.query(Habit).all()
        longest = AnalyticsService.find_longest_streak_all(all_habits)
        
        assert longest == 8
    
    def test_get_tracked_habits(self, test_db):
        """Test getting habit names"""
        habits = [
            Habit(name="Drink Water", specification="", periodicity="daily", created_at=datetime.now()),
            Habit(name="Exercise", specification="", periodicity="daily", created_at=datetime.now()),
        ]
        
        for h in habits:
            test_db.add(h)
        test_db.commit()
        
        all_habits = test_db.query(Habit).all()
        names = AnalyticsService.get_all_tracked_habits(all_habits)
        
        assert len(names) == 2
        assert "Drink Water" in names
    
    def test_struggling_habits(self, test_db):
        """Test finding struggling habits"""
        habit1 = Habit(name="Good", specification="", periodicity="daily", created_at=datetime.now())
        habit2 = Habit(name="Struggling", specification="", periodicity="daily", created_at=datetime.now())
        
        test_db.add_all([habit1, habit2])
        test_db.commit()
        
        now = datetime.now()
        
        # Habit 1: 5-day streak (good)
        for i in range(5):
            completion = Completion(habit_id=habit1.habit_id, completion_date=now - timedelta(days=i))
            test_db.add(completion)
        
        # Habit 2: 2-day streak (struggling)
        for i in range(2):
            completion = Completion(habit_id=habit2.habit_id, completion_date=now - timedelta(days=i))
            test_db.add(completion)
        
        test_db.commit()
        
        all_habits = test_db.query(Habit).all()
        struggling = AnalyticsService.get_struggling_habits(all_habits, threshold=3)
        
        assert len(struggling) == 1
        assert struggling[0].name == "Struggling"
        
        
    def test_update_habit(self, test_db):
        habit = HabitService.create_habit(test_db, "Read", "Book 1 chapter", "daily")
        updated = HabitService.update_habit(test_db, int(habit.habit_id), name="Read Bible", periodicity="weekly")
        assert updated.name == "Read Bible"
        assert updated.periodicity == "weekly"    
