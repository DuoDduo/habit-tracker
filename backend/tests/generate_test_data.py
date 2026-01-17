"""
Generate Test Data - 5 Predefined Habits with 4 Weeks of Data
Author: Blessing Oluwapelumi James
Matric No: 92134091

Run this script to populate the database with realistic test data.
Usage: python generate_test_data.py
"""

import sys
import os
from pathlib import Path

# Add backend to path
backend_path = Path(__file__).parent
sys.path.insert(0, str(backend_path))

from datetime import datetime, timedelta
import random
from app.db.session import SessionLocal, init_db
from app.models.habit import Habit, Completion


def clear_database(db):
    """Clear all existing data"""
    print("Clearing existing data...")
    db.query(Completion).delete()
    db.query(Habit).delete()
    db.commit()
    print("Database cleared")


def create_predefined_habits(db):
    """
    Create 5 predefined habits with different characteristics.
    
    Returns:
        List of created Habit objects
    """
    habits_data = [
        {
            "name": "Drink Water",
            "specification": "Drink 8 glasses of water throughout the day",
            "periodicity": "daily",
            "completion_rate": 0.9,  # 90% completion rate
            "description": "High compliance habit"
        },
        {
            "name": "Exercise",
            "specification": "Complete 30 minutes of physical activity",
            "periodicity": "daily",
            "completion_rate": 0.7,  # 70% completion rate
            "description": "Moderate compliance habit"
        },
        {
            "name": "Read Book",
            "specification": "Read for at least 20 minutes before bed",
            "periodicity": "daily",
            "completion_rate": 0.6,  # 60% completion rate
            "description": "Struggling habit"
        },
        {
            "name": "Weekly Review",
            "specification": "Review and plan weekly goals every Sunday",
            "periodicity": "weekly",
            "completion_rate": 1.0,  # Perfect compliance
            "description": "Perfect weekly habit"
        },
        {
            "name": "Meditation",
            "specification": "Practice 10 minutes of mindfulness meditation",
            "periodicity": "daily",
            "completion_rate": 0.8,  # 80% completion rate
            "description": "Good compliance habit"
        }
    ]
    
    created_habits = []
    
    print("\nCreating predefined habits...")
    for data in habits_data:
        habit = Habit(
            name=data["name"],
            specification=data["specification"],
            periodicity=data["periodicity"],
            created_at=datetime.now() - timedelta(days=28)  # Created 4 weeks ago
        )
        
        db.add(habit)
        db.commit()
        db.refresh(habit)
        
        created_habits.append({
            "habit": habit,
            "completion_rate": data["completion_rate"],
            "description": data["description"]
        })
        
        print(f"Created: {habit.name} ({habit.periodicity}) - {data['description']}")
    
    return created_habits


def generate_completions(db, habit_data_list):
    """
    Generate 4 weeks of realistic completion data for each habit.
    
    Args:
        db: Database session
        habit_data_list: List of dicts with habit and completion_rate
    """
    start_date = datetime.now() - timedelta(days=28)
    
    print("\nGenerating 4 weeks of completion data...")
    
    total_completions = 0
    
    for habit_data in habit_data_list:
        habit = habit_data["habit"]
        completion_rate = habit_data["completion_rate"]
        
        completions_count = 0
        
        if habit.periodicity == "daily":
            # Generate daily completions for 28 days
            for day in range(28):
                if random.random() < completion_rate:
                    # Random time during the day
                    completion_date = start_date + timedelta(days=day)
                    completion_date += timedelta(
                        hours=random.randint(6, 22),
                        minutes=random.randint(0, 59),
                        seconds=random.randint(0, 59)
                    )
                    
                    completion = Completion(
                        habit_id=habit.habit_id,
                        completion_date=completion_date
                    )
                    db.add(completion)
                    completions_count += 1
        
        elif habit.periodicity == "weekly":
            # Generate weekly completions for 4 weeks
            for week in range(4):
                if random.random() < completion_rate:
                    # Random day in the week (0-6)
                    day_in_week = random.randint(0, 6)
                    completion_date = start_date + timedelta(weeks=week, days=day_in_week)
                    completion_date += timedelta(
                        hours=random.randint(9, 18),
                        minutes=random.randint(0, 59),
                        seconds=random.randint(0, 59)
                    )
                    
                    completion = Completion(
                        habit_id=habit.habit_id,
                        completion_date=completion_date
                    )
                    db.add(completion)
                    completions_count += 1
        
        db.commit()
        total_completions += completions_count
        
        print(f"   {habit.name}: {completions_count} completions")
    
    print(f"\nTotal completions generated: {total_completions}")


def display_summary(db):
    """Display summary statistics"""
    habits = db.query(Habit).all()
    
    print("\n" + "=" * 60)
    print("HABIT TRACKER - TEST DATA SUMMARY")
    print("=" * 60)
    
    print(f"\nTotal Habits: {len(habits)}")
    
    daily_count = len([h for h in habits if h.periodicity == "daily"])
    weekly_count = len([h for h in habits if h.periodicity == "weekly"])
    
    print(f"   • Daily habits: {daily_count}")
    print(f"   • Weekly habits: {weekly_count}")
    
    print("\n Habit Details:")
    print("-" * 60)
    
    for habit in habits:
        current_streak = habit.calculate_current_streak()
        longest_streak = habit.calculate_longest_streak()
        is_broken = habit.is_broken()
        completion_count = len(habit.completions)
        
        status = "Broken" if is_broken else "Active"
        
        print(f"\n{habit.name} ({habit.periodicity})")
        print(f"   Current Streak: {current_streak}")
        print(f"   Longest Streak: {longest_streak}")
        print(f"   Completions: {completion_count}")
        print(f"   Status: {status}")
    
    # Overall statistics
    all_streaks = [h.calculate_longest_streak() for h in habits]
    longest_overall = max(all_streaks) if all_streaks else 0
    
    print("\n" + "-" * 60)
    print(f"Longest Streak Overall: {longest_overall}")
    print("=" * 60)


def main():
    """Main function to generate all test data"""
    print("\n" + "=" * 60)
    print("HABIT TRACKER - TEST DATA GENERATOR")
    print("=" * 60)
    print("Author: Blessing Oluwapelumi James")
    print("Matric No: 92134091")
    print("=" * 60)
    
    # Initialize database
    print("\nInitializing database...")
    init_db()
    print("Database initialized")
    
    # Create session
    db = SessionLocal()
    
    try:
        # Clear existing data
        clear_database(db)
        
        # Create predefined habits
        habit_data_list = create_predefined_habits(db)
        
        # Generate completions
        generate_completions(db, habit_data_list)
        
        # Display summary
        display_summary(db)
        
        print("\nTest data generation complete!")
        print("You can now start the application and see the data")
        print("\nNext steps:")
        print("  1. Run: python run.py")
        print("  2. Open frontend in browser")
        print("  3. Explore the 5 predefined habits\n")
        
    except Exception as e:
        print(f"\nError generating test data: {e}")
        db.rollback()
        raise
    
    finally:
        db.close()


if __name__ == "__main__":
    main()