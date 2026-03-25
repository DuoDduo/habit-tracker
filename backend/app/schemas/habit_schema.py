"""
Pydantic Schemas for Request/Response Validation
Author: Blessing Oluwapelumi James
Matric No: 92134091

These schemas provide automatic validation and documentation
for API requests and responses.
"""

# Import BaseModel and field utilities for schema validation
from pydantic import BaseModel, Field, field_validator, ConfigDict

# Import datetime for timestamp fields
from datetime import datetime

# Import typing for optional and list type hints
from typing import List, Optional


class HabitCreate(BaseModel):
    """
    Schema for creating a new habit.
    
    Validates that:
    - Name is required and between 1-255 characters
    - Periodicity is either "daily" or "weekly"
    """
    
    # Habit name: required, 1-255 characters, with description for docs
    name: str = Field(..., min_length=1, max_length=255, description="Habit name")
    
    # Optional detailed description of habit, max 500 characters
    specification: Optional[str] = Field(None, max_length=500, description="Task description")
    
    # Periodicity: required field, either 'daily' or 'weekly'
    periodicity: str = Field(..., description="Tracking Frequency: 'daily' or 'weekly'")
    
    @field_validator("periodicity")
    def validate_periodicity(cls, v):
        """Validate that periodicity is either 'daily' or 'weekly'"""
        if v not in ["daily", "weekly"]:
            raise ValueError("Periodicity must be 'daily' or 'weekly'")
        return v
    
    # Configuration for Pydantic model (for JSON schema & examples)
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
    
    habit_id: int  # Unique identifier
    name: str  # Habit name
    specification: Optional[str]  # Optional detailed description
    periodicity: str  # 'daily' or 'weekly'
    created_at: datetime  # Timestamp of creation
    current_streak: int  # Calculated current streak
    longest_streak: int  # Calculated longest streak
    is_broken: bool  # Whether habit was broken
    completion_count: int  # Total number of completions
    
    # Allow automatic population from ORM model attributes
    model_config = ConfigDict(from_attributes=True)


class HabitList(BaseModel):
    """Schema for list of habits"""
    
    habits: List[HabitResponse]  # List of habit responses
    total: int  # Total number of habits


class AnalyticsResponse(BaseModel):
    """Schema for analytics response"""
    
    # Optional fields because some analytics may be missing
    longest_streak: Optional[int] = None  # Highest streak among habits
    habit_names: Optional[List[str]] = None  # List of habit names
    daily_count: Optional[int] = None  # Number of daily habits
    weekly_count: Optional[int] = None  # Number of weekly habits
    total_habits: Optional[int] = None  # Total number of habits
    active_streaks: Optional[int] = None  # Count of currently active streaks
    broken_habits: Optional[int] = None  # Count of broken habits


class HabitUpdate(BaseModel):
    """
    Schema for updating an existing habit.
    
    All fields are optional; only provided fields are updated.
    """
    
    # Optional fields with validation limits
    name: Optional[str] = Field(None, min_length=1, max_length=255)
    specification: Optional[str] = Field(None, max_length=500)
    periodicity: Optional[str]  # Optional 'daily'/'weekly' update
    
    @field_validator("periodicity")
    def validate_periodicity(cls, v):
        """Validate that periodicity is None, 'daily', or 'weekly'"""
        if v not in [None, "daily", "weekly"]:
            raise ValueError("Periodicity must be 'daily' or 'weekly'")
        return v