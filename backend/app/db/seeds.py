"""
Database Seeding Utility
Author: Blessing Oluwapelumi James
Matric No: 92134091
"""

from datetime import datetime, timedelta
import random
from app.models.habit import Habit, Completion

def seed_predefined_habits(db):
    """
    Seed the database with 5 predefined habits if none exist.
    """
    if db.query(Habit).count() > 0:
        return

    print("Seeding database with predefined habits...")
    
    habits_data = [
        {
            "name": "Drink Water",
            "specification": "Drink 8 glasses of water throughout the day",
            "periodicity": "daily",
            "completion_rate": 0.9
        },
        {
            "name": "Exercise",
            "specification": "Complete 30 minutes of physical activity",
            "periodicity": "daily",
            "completion_rate": 0.7
        },
        {
            "name": "Read Book",
            "specification": "Read for at least 20 minutes before bed",
            "periodicity": "daily",
            "completion_rate": 0.6
        },
        {
            "name": "Weekly Review",
            "specification": "Review and plan weekly goals every Sunday",
            "periodicity": "weekly",
            "completion_rate": 1.0
        },
        {
            "name": "Meditation",
            "specification": "Practice 10 minutes of mindfulness meditation",
            "periodicity": "daily",
            "completion_rate": 0.8
        }
    ]
    
    start_date = datetime.now() - timedelta(days=28)
    
    for data in habits_data:
        habit = Habit(
            name=data["name"],
            specification=data["specification"],
            periodicity=data["periodicity"],
            created_at=start_date
        )
        db.add(habit)
        db.commit()
        db.refresh(habit)
        
        # Generate 4 weeks of random completion data
        rate = data["completion_rate"]
        for day in range(28):
            if habit.periodicity == "daily":
                if random.random() < rate:
                    c_date = start_date + timedelta(days=day, hours=random.randint(6, 22))
                    db.add(Completion(habit_id=habit.habit_id, completion_date=c_date))
            elif habit.periodicity == "weekly" and day % 7 == 0:
                if random.random() < rate:
                    c_date = start_date + timedelta(days=day + random.randint(0, 6), hours=random.randint(9, 18))
                    db.add(Completion(habit_id=habit.habit_id, completion_date=c_date))
        
        db.commit()

    print("Database seeding completed.")
