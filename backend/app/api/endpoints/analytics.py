"""
Analytics API Endpoints - Functional Programming
Author: Blessing Oluwapelumi James
Matric No: 92134091

This module exposes the functional programming analytics functions
through REST API endpoints.
"""

from flask import Blueprint, request, jsonify
from app.services.habit_service import HabitService
from app.services.analytics_service import AnalyticsService
from app.db.session import get_db
from typing import List

# Create Blueprint for analytics endpoints
analytics_bp = Blueprint("analytics", __name__, url_prefix="/api/analytics")


def habit_summary_dict(habit) -> dict:
    """
    Helper function to convert a Habit model instance
    into a summary dictionary for analytics endpoints.

    Includes:
    - habit_id, name, specification, periodicity
    - current_streak, longest_streak, completion_count
    """
    return {
        "habit_id": habit.habit_id,
        "name": habit.name,
        "specification": habit.specification,
        "periodicity": habit.periodicity,
        "current_streak": habit.calculate_current_streak(),
        "longest_streak": habit.calculate_longest_streak(),
        "completion_count": len(habit.completions)
    }


@analytics_bp.route("/longest-streak", methods=["GET"])
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
        with get_db() as db:
            habits = HabitService.get_all_habits(db)

        # Functional programming: find longest streak
        streak = AnalyticsService.find_longest_streak_all(habits)
        return jsonify({"longest_streak": streak}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@analytics_bp.route("/by-periodicity", methods=["GET"])
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
        period = request.args.get("period", "daily")
        if period not in ["daily", "weekly"]:
            return jsonify({"error": "Period must be 'daily' or 'weekly'"}), 400

        with get_db() as db:
            habits = HabitService.get_all_habits(db)

        filtered = AnalyticsService.get_habits_by_periodicity(habits, period)
        response = [habit_summary_dict(h) for h in filtered]

        return jsonify(response), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@analytics_bp.route("/tracked-habits", methods=["GET"])
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
        with get_db() as db:
            habits = HabitService.get_all_habits(db)

        # Functional programming: get all names
        names: List[str] = AnalyticsService.get_all_tracked_habits(habits)
        return jsonify({"habits": names}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@analytics_bp.route("/struggling", methods=["GET"])
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
        threshold = int(request.args.get("threshold", 3))
        with get_db() as db:
            habits = HabitService.get_all_habits(db)

        struggling = AnalyticsService.get_struggling_habits(habits, threshold)
        response = [habit_summary_dict(h) for h in struggling]

        return jsonify(response), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@analytics_bp.route("/summary", methods=["GET"])
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
        with get_db() as db:
            habits = HabitService.get_all_habits(db)

        counts = AnalyticsService.count_by_periodicity(habits)
        longest = AnalyticsService.find_longest_streak_all(habits)

        active_count = len(list(filter(lambda h: not h.is_broken(), habits)))
        broken_count = len(list(filter(lambda h: h.is_broken(), habits)))

        response = {
            "total_habits": len(habits),
            "daily_habits": counts["daily"],
            "weekly_habits": counts["weekly"],
            "longest_streak": longest,
            "active_streaks": active_count,
            "broken_habits": broken_count
        }

        return jsonify(response), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500