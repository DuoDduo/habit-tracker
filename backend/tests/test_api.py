"""
Tests for API Endpoints
Author: Blessing Oluwapelumi James
Matric No: 92134091

Integration tests for REST API.
Total: 15 tests
"""

import pytest
import json


class TestHabitsAPI:
    """Test habit API endpoints"""
    
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
    
    def test_get_habit_endpoint(self, test_client):
        """Test GET /api/habits/:id"""
        # Create habit first
        create_response = test_client.post(
            "/api/habits",
            data=json.dumps({
                "name": "Get Test",
                "specification": "",
                "periodicity": "daily"
            }),
            content_type="application/json"
        )
        habit_id = json.loads(create_response.data)["habit_id"]
        
        # Get habit
        response = test_client.get(f"/api/habits/{habit_id}")
        
        assert response.status_code == 200
        data = json.loads(response.data)
        assert data["name"] == "Get Test"
    
    def test_delete_habit_endpoint(self, test_client):
        """Test DELETE /api/habits/:id"""
        # Create habit
        create_response = test_client.post(
            "/api/habits",
            data=json.dumps({
                "name": "Delete Test",
                "specification": "",
                "periodicity": "daily"
            }),
            content_type="application/json"
        )
        habit_id = json.loads(create_response.data)["habit_id"]
        
        # Delete
        response = test_client.delete(f"/api/habits/{habit_id}")
        
        assert response.status_code == 200
        
        # Verify deleted
        get_response = test_client.get(f"/api/habits/{habit_id}")
        assert get_response.status_code == 404
    
    def test_check_off_endpoint(self, test_client):
        """Test POST /api/habits/:id/check-off"""
        # Create habit
        create_response = test_client.post(
            "/api/habits",
            data=json.dumps({
                "name": "Check Off Test",
                "specification": "",
                "periodicity": "daily"
            }),
            content_type="application/json"
        )
        habit_id = json.loads(create_response.data)["habit_id"]
        
        # Check off
        response = test_client.post(f"/api/habits/{habit_id}/check-off")
        
        assert response.status_code == 200
        data = json.loads(response.data)
        assert data["completion_count"] == 1
        
    def test_update_habit_endpoint(self, test_client):
        # Assuming habit already exists
        response = test_client.patch("/api/habits/1", json={"name": "Updated Habit", "periodicity": "weekly"})
        assert response.status_code == 200
        assert response.json["name"] == "Updated Habit"  


class TestAnalyticsAPI:
    """Test analytics API endpoints"""
    
    def test_longest_streak_endpoint(self, test_client):
        """Test GET /api/analytics/longest-streak"""
        response = test_client.get("/api/analytics/longest-streak")
        
        assert response.status_code == 200
        data = json.loads(response.data)
        assert "longest_streak" in data
    
    def test_by_periodicity_endpoint(self, test_client):
        """Test GET /api/analytics/by-periodicity"""
        response = test_client.get("/api/analytics/by-periodicity?period=daily")
        
        assert response.status_code == 200
        data = json.loads(response.data)
        assert isinstance(data, list)
    
    def test_tracked_habits_endpoint(self, test_client):
        """Test GET /api/analytics/tracked-habits"""
        response = test_client.get("/api/analytics/tracked-habits")
        
        assert response.status_code == 200
        data = json.loads(response.data)
        assert "habits" in data
    
    def test_summary_endpoint(self, test_client):
        """Test GET /api/analytics/summary"""
        response = test_client.get("/api/analytics/summary")
        
        assert response.status_code == 200
        data = json.loads(response.data)
        assert "total_habits" in data
        assert "longest_streak" in data