"""
Pydantic Schemas for Request/Response Validation
Author: Blessing Oluwapelumi James
Matric No: 92134091

These schemas provide automatic validation and documentation
for API requests and responses.
"""

from pydantic import BaseModel, Field, field_validator,ConfigDict
from datetime import datetime
from typing import List, Optional


class HabitCreate(BaseModel):
    """
    Schema for creating a new habit.
    
    Validates that:
    - Name is required and between 1-255 characters
    - Periodicity is either "daily" or "weekly"
    """
    name: str = Field(..., min_length=1, max_length=255, description="Habit name")
    specification: Optional[str] = Field(None, max_length=500, description="Task description")
    periodicity: str = Field(..., description="Tracking Frequency: 'daily' or 'weekly'")
    
    @field_validator("periodicity")
    def validate_periodicity(cls, v):
        """Validate periodicity is daily or weekly"""
        if v not in ["daily", "weekly"]:
            raise ValueError("Periodicity must be 'daily' or 'weekly'")
        return v
    
    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "name": "Drink Water",
                "specification": "Drink 8 glasses of water throughout the day",
                "periodicity": "daily"
            }
        }
    )


class HabitResponse(BaseModel):
    """
    Schema for habit response.
    
    Includes all habit data plus calculated fields
    like streaks and completion count.
    """
    habit_id: int
    name: str
    specification: Optional[str]
    periodicity: str
    created_at: datetime
    current_streak: int
    longest_streak: int
    is_broken: bool
    completion_count: int
    
    model_config = ConfigDict(from_attributes=True)


class HabitList(BaseModel):
    """Schema for list of habits"""
    habits: List[HabitResponse]
    total: int


class AnalyticsResponse(BaseModel):
    """Schema for analytics response"""
    longest_streak: Optional[int] = None
    habit_names: Optional[List[str]] = None
    daily_count: Optional[int] = None
    weekly_count: Optional[int] = None
    total_habits: Optional[int] = None
    active_streaks: Optional[int] = None
    broken_habits: Optional[int] = None

class HabitUpdate(BaseModel):
    name: Optional[str] = Field(None, min_length=1, max_length=255)
    specification: Optional[str] = Field(None, max_length=500)
    periodicity: Optional[str]

    @field_validator("periodicity")
    def validate_periodicity(cls, v):
        if v not in [None, "daily", "weekly"]:
            raise ValueError("Periodicity must be 'daily' or 'weekly'")
        return v