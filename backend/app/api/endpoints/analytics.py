"""
Analytics API Endpoints - Functional Programming
Author: Blessing Oluwapelumi James
Matric No: 92134091

This module exposes the functional programming analytics functions
through REST API endpoints.
"""

# Import Blueprint to modularize routes, request to access query parameters,
# and jsonify to convert Python objects into JSON HTTP responses
from flask import Blueprint, request, jsonify

# Import HabitService to interact with habit-related database operations
from app.services.habit_service import HabitService

# Import AnalyticsService which contains functional programming analytics logic
from app.services.analytics_service import AnalyticsService

# Import database session context manager for safe DB access
from app.db.session import get_db

# Import List type for type hinting
from typing import List


# Create Blueprint for analytics endpoints
# This groups all analytics routes under a common URL prefix
analytics_bp = Blueprint("analytics", __name__, url_prefix="/api/analytics")


def habit_summary_dict(habit) -> dict:
    """
    Helper function to convert a Habit model instance
    into a summary dictionary for analytics endpoints.

    Includes:
    - habit_id, name, specification, periodicity
    - current_streak, longest_streak, completion_count
    """
    # Return a dictionary representation of a Habit object
    # This ensures consistent API response formatting
    return {
        "habit_id": habit.habit_id,  # Unique identifier of the habit
        "name": habit.name,  # Name/title of the habit
        "specification": habit.specification,  # Description or details of the habit
        "periodicity": habit.periodicity,  # Frequency (daily/weekly)
        "current_streak": habit.calculate_current_streak(),  # Dynamically compute current streak
        "longest_streak": habit.calculate_longest_streak(),  # Dynamically compute longest streak
        "completion_count": len(habit.completions)  # Total number of recorded completions
    }


@analytics_bp.route("/longest-streak", methods=["GET"])  # Define GET endpoint
def longest_streak():
    """
    GET /api/analytics/longest-streak
    Get the longest streak across all habits.
    Uses functional programming: map() and max()
    ---
    tags:
      - Analytics
    responses:
      200:
        description: The highest streak count achieved among all tracked habits
        schema:
          properties:
            longest_streak:
              type: integer
              example: 21
    """
    try:
        # Open database session safely using context manager
        with get_db() as db:
            # Retrieve all habits from the database
            habits = HabitService.get_all_habits(db)

        # Functional programming logic delegated to AnalyticsService
        # Computes the maximum streak among all habits
        streak = AnalyticsService.find_longest_streak_all(habits)

        # Return JSON response with HTTP 200 OK
        return jsonify({"longest_streak": streak}), 200

    except Exception as e:
        # Handle unexpected errors and return HTTP 500 Internal Server Error
        return jsonify({"error": str(e)}), 500


@analytics_bp.route("/by-periodicity", methods=["GET"])  # Define GET endpoint
def habits_by_periodicity():
    """
    GET /api/analytics/by-periodicity?period=daily
    Get habits filtered by periodicity.
    Uses functional programming: filter() with lambda
    ---
    tags:
      - Analytics
    parameters:
      - name: period
        in: query
        type: string
        enum: ['daily', 'weekly']
        required: false
        default: daily
        description: Filter habits by their frequency
    responses:
      200:
        description: A list of habits matching the specified period
    """
    try:
        # Get 'period' query parameter from URL, default to 'daily'
        period = request.args.get("period", "daily")

        # Validate allowed values
        if period not in ["daily", "weekly"]:
            # Return 400 Bad Request if invalid value provided
            return jsonify({"error": "Period must be 'daily' or 'weekly'"}), 400

        # Open database session
        with get_db() as db:
            # Retrieve all habits
            habits = HabitService.get_all_habits(db)

        # Apply functional filtering logic via AnalyticsService
        filtered = AnalyticsService.get_habits_by_periodicity(habits, period)

        # Convert filtered Habit objects to summary dictionaries
        response = [habit_summary_dict(h) for h in filtered]

        # Return filtered results
        return jsonify(response), 200

    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": str(e)}), 500


@analytics_bp.route("/tracked-habits", methods=["GET"])  # Define GET endpoint
def tracked_habits():
    """
    Get list of all tracked habit names.
    ---
    tags:
      - Analytics
    responses:
      200:
        description: An array containing the names of all active habits
        schema:
          properties:
            habits:
              type: array
              items:
                type: string
                example: ["Drink Water", "Exercise"]
    """
    try:
        # Open database session
        with get_db() as db:
            # Retrieve all habits
            habits = HabitService.get_all_habits(db)

        # Functional programming approach to extract habit names
        names: List[str] = AnalyticsService.get_all_tracked_habits(habits)

        # Return names in JSON format
        return jsonify({"habits": names}), 200

    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": str(e)}), 500


@analytics_bp.route("/struggling", methods=["GET"])  # Define GET endpoint
def struggling_habits():
    """
    GET /api/analytics/struggling?threshold=3
    Get habits with current streak below threshold.
    ---
    tags:
      - Analytics
    parameters:
      - name: threshold
        in: query
        type: integer
        required: false
        default: 3
        description: Minimum streak count to NOT be considered struggling
    responses:
      200:
        description: List of habits currently underperforming
    """
    try:
        # Get threshold parameter and convert to integer
        threshold = int(request.args.get("threshold", 3))

        # Open database session
        with get_db() as db:
            # Retrieve all habits
            habits = HabitService.get_all_habits(db)

        # Use functional logic to determine struggling habits
        struggling = AnalyticsService.get_struggling_habits(habits, threshold)

        # Convert Habit objects to dictionary format
        response = [habit_summary_dict(h) for h in struggling]

        # Return struggling habits list
        return jsonify(response), 200

    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": str(e)}), 500


@analytics_bp.route("/summary", methods=["GET"])  # Define GET endpoint
def analytics_summary():
    """
    Get comprehensive analytics summary.
    ---
    tags:
      - Analytics
    responses:
      200:
        description: Consolidated metrics for the dashboard
        schema:
          properties:
            total_habits: {type: integer}
            daily_habits: {type: integer}
            weekly_habits: {type: integer}
            longest_streak: {type: integer}
            active_streaks: {type: integer}
            broken_habits: {type: integer}
    """
    try:
        # Open database session
        with get_db() as db:
            # Retrieve all habits
            habits = HabitService.get_all_habits(db)

        # Count habits grouped by periodicity (daily/weekly)
        counts = AnalyticsService.count_by_periodicity(habits)

        # Compute longest streak across all habits
        longest = AnalyticsService.find_longest_streak_all(habits)

        # Functional programming: filter active habits (not broken)
        active_count = len(list(filter(lambda h: not h.is_broken(), habits)))

        # Functional programming: filter broken habits
        broken_count = len(list(filter(lambda h: h.is_broken(), habits)))

        # Build consolidated analytics response dictionary
        response = {
            "total_habits": len(habits),  # Total number of habits
            "daily_habits": counts["daily"],  # Count of daily habits
            "weekly_habits": counts["weekly"],  # Count of weekly habits
            "longest_streak": longest,  # Highest streak achieved
            "active_streaks": active_count,  # Number of habits currently active
            "broken_habits": broken_count  # Number of habits with broken streaks
        }

        # Return analytics summary
        return jsonify(response), 200

    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": str(e)}), 500