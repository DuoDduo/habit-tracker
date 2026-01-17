"""
Analytics API Endpoints - Functional Programming
Author: Blessing Oluwapelumi James
Matric No: 92134091
"""

from flask import Blueprint, request, jsonify
from app.services.habit_service import HabitService
from app.services.analytics_service import AnalyticsService
from app.db.session import get_db

analytics_bp = Blueprint("analytics", __name__, url_prefix="/api/analytics")


@analytics_bp.route("/longest-streak", methods=["GET"])
def longest_streak():
    """
    Get the longest streak across all habits.
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
        db = next(get_db())
        habits = HabitService.get_all_habits(db)
        
        # Use functional programming
        streak = AnalyticsService.find_longest_streak_all(habits)
        
        return jsonify({"longest_streak": streak}), 200
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@analytics_bp.route("/by-periodicity", methods=["GET"])
def habits_by_periodicity():
    """
    Get habits filtered by periodicity.
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
        schema:
          type: array
          items:
            properties:
              habit_id: {type: integer}
              name: {type: string}
              periodicity: {type: string}
              current_streak: {type: integer}
    """
    try:
        period = request.args.get("period", "daily")
        
        if period not in ["daily", "weekly"]:
            return jsonify({"error": "Period must be 'daily' or 'weekly'"}), 400
        
        db = next(get_db())
        habits = HabitService.get_all_habits(db)
        
        # Use functional programming
        filtered = AnalyticsService.get_habits_by_periodicity(habits, period)
        
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
            for h in filtered
        ]
        
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
        db = next(get_db())
        habits = HabitService.get_all_habits(db)
        
        # Use functional programming
        names = AnalyticsService.get_all_tracked_habits(habits)
        
        return jsonify({"habits": names}), 200
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@analytics_bp.route("/struggling", methods=["GET"])
def struggling_habits():
    """
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
        
        db = next(get_db())
        habits = HabitService.get_all_habits(db)
        
        # Use functional programming
        struggling = AnalyticsService.get_struggling_habits(habits, threshold)
        
        response = [
            {
                "habit_id": h.habit_id,
                "name": h.name,
                "specification": h.specification,
                "periodicity": h.periodicity,
                "current_streak": h.calculate_current_streak(),
                "longest_streak": h.calculate_longest_streak(),
                "completion_count": len(h.completions)
            }
            for h in struggling
        ]
        
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
        db = next(get_db())
        habits = HabitService.get_all_habits(db)
        
        # Use functional programming for all calculations
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