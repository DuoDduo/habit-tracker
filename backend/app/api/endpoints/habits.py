"""
Habits API Endpoints
Author: Blessing Oluwapelumi James
Matric No: 92134091
"""

from flask import Blueprint, request, jsonify
from app.services.habit_service import HabitService
from app.schemas.habit_schema import HabitCreate, HabitResponse
from app.db.session import get_db
from pydantic import ValidationError
from datetime import datetime

habits_bp = Blueprint("habits", __name__, url_prefix="/api/habits")


@habits_bp.route("", methods=["GET"])
def list_habits():
    """
    GET /api/habits
    Get all habits with their current status.
    """
    try:
        db = next(get_db())
        habits = HabitService.get_all_habits(db)
        
        response = [
            {
                "habit_id": h.habit_id,
                "name": h.name,
                "specification": h.specification,
                "periodicity": h.periodicity,
                "created_at": h.created_at.isoformat(),
                "current_streak": h.calculate_current_streak(),
                "longest_streak": h.calculate_longest_streak(),
                "is_broken": h.is_broken(),
                "completion_count": len(h.completions)
            }
            for h in habits
        ]
        
        return jsonify(response), 200
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@habits_bp.route("", methods=["POST"])
def create_habit():
    """
    POST /api/habits
    Create a new habit.
    
    Request Body:
    {
        "name": "Drink Water",
        "specification": "Drink 8 glasses",
        "periodicity": "daily"
    }
    """
    try:
        data = request.get_json()
        
        # Validate with Pydantic
        habit_data = HabitCreate(**data)
        
        db = next(get_db())
        habit = HabitService.create_habit(db, habit_data)
        
        response = {
            "habit_id": habit.habit_id,
            "name": habit.name,
            "specification": habit.specification,
            "periodicity": habit.periodicity,
            "created_at": habit.created_at.isoformat(),
            "current_streak": 0,
            "longest_streak": 0,
            "is_broken": True,
            "completion_count": 0
        }
        
        return jsonify(response), 201
    
    except ValidationError as e:
        return jsonify({"error": "Validation error", "details": e.errors()}), 400
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@habits_bp.route("/<int:habit_id>", methods=["GET"])
def get_habit(habit_id: int):
    """
    GET /api/habits/:id
    Get a specific habit by ID.
    """
    try:
        db = next(get_db())
        habit = HabitService.get_habit_by_id(db, habit_id)
        
        if not habit:
            return jsonify({"error": "Habit not found"}), 404
        
        response = {
            "habit_id": habit.habit_id,
            "name": habit.name,
            "specification": habit.specification,
            "periodicity": habit.periodicity,
            "created_at": habit.created_at.isoformat(),
            "current_streak": habit.calculate_current_streak(),
            "longest_streak": habit.calculate_longest_streak(),
            "is_broken": habit.is_broken(),
            "completion_count": len(habit.completions),
            "completions": [c.completion_date.isoformat() for c in habit.completions]
        }
        
        return jsonify(response), 200
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@habits_bp.route("/<int:habit_id>", methods=["DELETE"])
def delete_habit(habit_id: int):
    """
    DELETE /api/habits/:id
    Delete a habit and all its completions.
    """
    try:
        db = next(get_db())
        success = HabitService.delete_habit(db, habit_id)
        
        if not success:
            return jsonify({"error": "Habit not found"}), 404
        
        return jsonify({"message": "Habit deleted successfully"}), 200
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@habits_bp.route("/<int:habit_id>/check-off", methods=["POST"])
def check_off_habit(habit_id: int):
    """
    POST /api/habits/:id/check-off
    Mark a habit as completed for now (or specified time).
    
    Optional Request Body:
    {
        "timestamp": "2024-01-15T10:30:00"  // ISO format
    }
    """
    try:
        data = request.get_json() or {}
        timestamp = None
        
        if "timestamp" in data:
            timestamp = datetime.fromisoformat(data["timestamp"])
        
        db = next(get_db())
        habit = HabitService.check_off_habit(db, habit_id, timestamp)
        
        if not habit:
            return jsonify({"error": "Habit not found"}), 404
        
        response = {
            "habit_id": habit.habit_id,
            "name": habit.name,
            "specification": habit.specification,
            "periodicity": habit.periodicity,
            "created_at": habit.created_at.isoformat(),
            "current_streak": habit.calculate_current_streak(),
            "longest_streak": habit.calculate_longest_streak(),
            "is_broken": habit.is_broken(),
            "completion_count": len(habit.completions)
        }
        
        return jsonify(response), 200
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500