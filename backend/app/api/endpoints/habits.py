"""
Habits API Endpoints
Author: Blessing Oluwapelumi James
Matric No: 92134091

This module contains all REST API endpoints for habit CRUD operations.
"""

from flask import Blueprint, request, jsonify
from app.services.habit_service import HabitService
from app.schemas.habit_schema import HabitCreate
from app.db.session import get_db
from pydantic import ValidationError
from datetime import datetime, timezone
from dateutil.parser import isoparse  # For robust ISO timestamp parsing
from typing import Optional

# Create Blueprint for habits endpoints
habits_bp = Blueprint("habits", __name__, url_prefix="/api/habits")


def habit_to_dict(habit) -> dict:
    """
    Helper function to convert a Habit model instance
    into a dictionary suitable for JSON response.
    
    Includes:
    - habit_id, name, specification, periodicity
    - created_at (ISO format)
    - current_streak, longest_streak, is_broken
    - completion_count
    - completions (list of ISO timestamps)
    """
    return {
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


@habits_bp.route("", methods=["GET"])
def list_habits():
    """
    GET /api/habits
    Get all habits with their current status.
    ---
    responses:
      200:
        description: A list of all habits and their current performance metrics
    """
    try:
        with get_db() as db:
            habits = HabitService.get_all_habits(db)

        response = [habit_to_dict(h) for h in habits]
        return jsonify(response), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@habits_bp.route("", methods=["POST"])
def create_habit():
    """
    POST /api/habits
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
        data = request.get_json() or {}
        habit_data = HabitCreate(**data)  # Full Pydantic validation

        with get_db() as db:
            habit = HabitService.create_habit(
                db=db,
                name=habit_data.name,
                specification=habit_data.specification or "",
                periodicity=habit_data.periodicity
            )

        response = habit_to_dict(habit)
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
        with get_db() as db:
            habit = HabitService.get_habit_by_id(db, habit_id)

        if not habit:
            return jsonify({"error": "Habit not found"}), 404

        response = habit_to_dict(habit)
        return jsonify(response), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@habits_bp.route("/<int:habit_id>", methods=["DELETE"])
def delete_habit(habit_id: int):
    """
    DELETE /api/habits/:id
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
        with get_db() as db:
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
      400:
        description: Invalid timestamp
      404:
        description: Habit not found
    """
    try:
        data = request.get_json(silent=True) or {}
        timestamp: Optional[datetime] = None

        # Parse timestamp if provided
        if "timestamp" in data:
            try:
                timestamp = isoparse(data["timestamp"])
            except ValueError:
                return jsonify({"error": "Invalid timestamp format"}), 400

        with get_db() as db:
            habit = HabitService.check_off_habit(db, habit_id, timestamp if timestamp is not None else datetime.now(timezone.utc))

        if not habit:
            return jsonify({"error": "Habit not found"}), 404

        response = habit_to_dict(habit)
        return jsonify(response), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
      
@habits_bp.route("/<int:habit_id>", methods=["PATCH"])
def update_habit(habit_id: int):
    """
    PATCH /api/habits/{id}:
    summary: Update a habit
    parameters:
      - name: id
        in: path
        required: true
        type: integer
    requestBody:
      required: true
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/HabitUpdate'
    responses:
      200:
        description: Habit updated successfully
      400:
        description: Validation error
      404:
        description: Habit not found
    """
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "Request body is required"}), 400
        
        # Validate using Pydantic
        from app.schemas.habit_schema import HabitUpdate
        habit_data = HabitUpdate(**data)
        
        with get_db() as db:
            habit = HabitService.update_habit(db, habit_id, **habit_data.dict(exclude_unset=True))
        
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
    except ValidationError as e:
        return jsonify({"error": "Validation error", "details": e.errors()}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500      
      