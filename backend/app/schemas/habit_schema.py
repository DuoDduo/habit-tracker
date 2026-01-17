"""
Pydantic Schemas for Request/Response Validation
Author: Blessing Oluwapelumi James
Matric No: 92134091
"""

from pydantic import BaseModel, Field, validator
from datetime import datetime
from typing import List, Optional


class HabitCreate(BaseModel):
    """Schema for creating a new habit"""
    name: str = Field(..., min_length=1, max_length=255, description="Habit name")
    specification: Optional[str] = Field(None, max_length=500, description="Task description")
    periodicity: str = Field(..., description="daily or weekly")
    
    @validator("periodicity")
    def validate_periodicity(cls, v):
        if v not in ["daily", "weekly"]:
            raise ValueError("Periodicity must be 'daily' or 'weekly'")
        return v
    
    class Config:
        json_schema_extra = {
            "example": {
                "name": "Drink Water",
                "specification": "Drink 8 glasses of water throughout the day",
                "periodicity": "daily"
            }
        }


class HabitResponse(BaseModel):
    """Schema for habit response"""
    habit_id: int
    name: str
    specification: Optional[str]
    periodicity: str
    created_at: datetime
    current_streak: int
    longest_streak: int
    is_broken: bool
    completion_count: int
    
    class Config:
        from_attributes = True


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