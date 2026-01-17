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
    Get all habits with their current status.
    ---
    responses:
      200:
        description: A list of all habits and their current performance metrics
        schema:
          type: array
          items:
            properties:
              habit_id: {type: integer}
              name: {type: string}
              periodicity: {type: string}
              current_streak: {type: integer}
              is_broken: {type: boolean}
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
    Create a new habit.
    ---
    parameters:
      - name: body
        in: body
        required: true
        schema:
          id: HabitCreate
          required:
            - name
            - periodicity
          properties:
            name: {type: string, example: "Read Bible"}
            specification: {type: string, example: "Read 2 chapters"}
            periodicity: {type: string, enum: [daily, weekly], example: "daily"}
    responses:
      201:
        description: Habit successfully created
      400:
        description: Validation error
    """
    try:
        data = request.get_json()
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
    Get a specific habit by ID.
    ---
    parameters:
      - name: habit_id
        in: path
        type: integer
        required: true
    responses:
      200:
        description: Detailed habit information including history
      404:
        description: Habit not found
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
    Delete a habit and all its completions.
    ---
    parameters:
      - name: habit_id
        in: path
        type: integer
        required: true
    responses:
      200:
        description: Habit deleted successfully
      404:
        description: Habit not found
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
    Mark a habit as completed.
    ---
    parameters:
      - name: habit_id
        in: path
        type: integer
        required: true
      - name: body
        in: body
        schema:
          properties:
            timestamp: {type: string, format: date-time, example: "2026-01-17T10:30:00"}
    responses:
      200:
        description: Habit checked off and streak updated
      404:
        description: Habit not found
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