"""
Habits API Endpoints
Author: Blessing Oluwapelumi James
Matric No: 92134091

This module contains all REST API endpoints for habit CRUD operations.
"""

# Import Blueprint to modularize route groups,
# request to access incoming HTTP data,
# and jsonify to convert Python objects into JSON responses
from flask import Blueprint, request, jsonify

# Import HabitService which contains business logic for habit operations
from app.services.habit_service import HabitService

# Import Pydantic schema for validating habit creation input
from app.schemas.habit_schema import HabitCreate

# Import database session context manager for safe database access
from app.db.session import get_db

# Import ValidationError to handle Pydantic validation failures
from pydantic import ValidationError

# Import datetime utilities for timestamp handling
from datetime import datetime, timezone

# Import isoparse for robust ISO 8601 timestamp parsing
from dateutil.parser import isoparse  # For robust ISO timestamp parsing

# Import Optional type for nullable timestamp hinting
from typing import Optional


# Create Blueprint for habits endpoints
# All routes here will be prefixed with /api/habits
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
    # Convert Habit ORM object into serializable dictionary format
    return {
        "habit_id": habit.habit_id,  # Unique identifier of the habit
        "name": habit.name,  # Name/title of the habit
        "specification": habit.specification,  # Detailed description
        "periodicity": habit.periodicity,  # Frequency (daily or weekly)
        "created_at": habit.created_at.isoformat(),  # Convert datetime to ISO 8601 string
        "current_streak": habit.calculate_current_streak(),  # Dynamically compute current streak
        "longest_streak": habit.calculate_longest_streak(),  # Dynamically compute longest streak
        "is_broken": habit.is_broken(),  # Boolean indicating if streak is broken
        "completion_count": len(habit.completions),  # Total completion records
        "completions": [c.completion_date.isoformat() for c in habit.completions]  # List of completion timestamps
    }


@habits_bp.route("", methods=["GET"])  # Define GET endpoint at /api/habits
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
        # Open database session safely
        with get_db() as db:
            # Retrieve all habits from database
            habits = HabitService.get_all_habits(db)

        # Convert Habit objects into dictionary format
        response = [habit_to_dict(h) for h in habits]

        # Return list of habits with HTTP 200 OK
        return jsonify(response), 200

    except Exception as e:
        # Handle unexpected server errors
        return jsonify({"error": str(e)}), 500


@habits_bp.route("", methods=["POST"])  # Define POST endpoint at /api/habits
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
        # Parse JSON request body safely
        data = request.get_json() or {}

        # Validate input using Pydantic schema
        habit_data = HabitCreate(**data)  # Full Pydantic validation

        # Open database session
        with get_db() as db:
            # Create habit using service layer
            habit = HabitService.create_habit(
                db=db,
                name=habit_data.name,
                specification=habit_data.specification or "",  # Default to empty string if None
                periodicity=habit_data.periodicity
            )

        # Convert created habit to dictionary
        response = habit_to_dict(habit)

        # Return created resource with HTTP 201 Created
        return jsonify(response), 201

    except ValidationError as e:
        # Handle Pydantic validation errors
        return jsonify({"error": "Validation error", "details": e.errors()}), 400

    except Exception as e:
        # Handle unexpected server errors
        return jsonify({"error": str(e)}), 500


@habits_bp.route("/<int:habit_id>", methods=["GET"])  # Define GET endpoint with path parameter
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
        # Open database session
        with get_db() as db:
            # Retrieve habit by ID
            habit = HabitService.get_habit_by_id(db, habit_id)

        # Return 404 if habit does not exist
        if not habit:
            return jsonify({"error": "Habit not found"}), 404

        # Convert to dictionary format
        response = habit_to_dict(habit)

        # Return habit data
        return jsonify(response), 200

    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": str(e)}), 500


@habits_bp.route("/<int:habit_id>", methods=["DELETE"])  # Define DELETE endpoint
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
        # Open database session
        with get_db() as db:
            # Attempt to delete habit
            success = HabitService.delete_habit(db, habit_id)

        # Return 404 if deletion failed (habit not found)
        if not success:
            return jsonify({"error": "Habit not found"}), 404

        # Return success message
        return jsonify({"message": "Habit deleted successfully"}), 200

    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": str(e)}), 500


@habits_bp.route("/<int:habit_id>/check-off", methods=["POST"])  # Define POST endpoint for completion
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
        # Safely parse JSON body
        data = request.get_json(silent=True) or {}

        # Initialize optional timestamp
        timestamp: Optional[datetime] = None

        # Parse timestamp if provided in request body
        if "timestamp" in data:
            try:
                # Convert ISO string to datetime object
                timestamp = isoparse(data["timestamp"])
            except ValueError:
                # Return 400 if invalid timestamp format
                return jsonify({"error": "Invalid timestamp format"}), 400

        # Open database session
        with get_db() as db:
            # Check off habit using provided timestamp or current UTC time
            habit = HabitService.check_off_habit(
                db,
                habit_id,
                timestamp if timestamp is not None else datetime.now(timezone.utc)
            )

        # Return 404 if habit does not exist
        if not habit:
            return jsonify({"error": "Habit not found"}), 404

        # Convert updated habit to dictionary
        response = habit_to_dict(habit)

        # Return updated habit data
        return jsonify(response), 200

    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": str(e)}), 500
      

@habits_bp.route("/<int:habit_id>", methods=["PATCH"])  # Define PATCH endpoint for updates
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
        # Parse request body
        data = request.get_json()

        # Ensure body is provided
        if not data:
            return jsonify({"error": "Request body is required"}), 400
        
        # Import HabitUpdate schema locally to avoid circular imports
        from app.schemas.habit_schema import HabitUpdate

        # Validate update data using Pydantic
        habit_data = HabitUpdate(**data)
        
        # Open database session
        with get_db() as db:
            # Update habit with only provided fields
            habit = HabitService.update_habit(
                db,
                habit_id,
                **habit_data.dict(exclude_unset=True)
            )
        
        # Return 404 if habit not found
        if not habit:
            return jsonify({"error": "Habit not found"}), 404
        
        # Manually construct response dictionary
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

        # Return updated habit
        return jsonify(response), 200

    except ValidationError as e:
        # Handle validation errors
        return jsonify({"error": "Validation error", "details": e.errors()}), 400

    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": str(e)}), 500