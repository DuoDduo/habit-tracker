"""
Tests for API Endpoints
Author: Blessing Oluwapelumi James
Matric No: 92134091
"""

import pytest
import json


class TestHabitsAPI:
    """Tests for habits endpoints"""
    
    def test_create_habit_endpoint(self, test_client):
        """Test POST /api/habits"""
        response = test_client.post(
            "/api/habits",
            data=json.dumps({
                "name": "API Test Habit",
                "specification": "Created via API",
                "periodicity": "daily"
            }),
            content_type="application/json"
        )
        
        assert response.status_code == 201
        data = json.loads(response.data)
        assert data["name"] == "API Test Habit"
        assert "habit_id" in data
    
    def test_list_habits_endpoint(self, test_client):
        """Test GET /api/habits"""
        response = test_client.get("/api/habits")
        
        assert response.status_code == 200
        data = json.loads(response.data)
        assert isinstance(data, list)


class TestAnalyticsAPI:
    """Tests for analytics endpoints"""
    
    def test_longest_streak_endpoint(self, test_client):
        """Test GET /api/analytics/longest-streak"""
        response = test_client.get("/api/analytics/longest-streak")
        
        assert response.status_code == 200
        data = json.loads(response.data)
        assert "longest_streak" in data
        assert isinstance(data["longest_streak"], int)