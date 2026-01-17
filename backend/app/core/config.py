"""
Configuration Management
Author: Blessing Oluwapelumi James
Matric No: 92134091
"""

from pydantic_settings import BaseSettings
from typing import Optional
import os
from pathlib import Path


class Settings(BaseSettings):
    """
    Application settings loaded from environment variables.
    Uses Pydantic for validation and type safety.
    """
    
    # Database
    DATABASE_URL: str = "sqlite:///../data/habits.db"
    
    # Flask
    FLASK_ENV: str = "development"
    FLASK_DEBUG: bool = True
    SECRET_KEY: str = "dev-secret-key-change-in-production"
    
    # Server
    HOST: str = "0.0.0.0"
    PORT: int = 5000
    
    # CORS
    CORS_ORIGINS: list = ["http://localhost:3000", "http://localhost:8000"]
    
    class Config:
        env_file = ".env"
        case_sensitive = True


# Global settings instance
settings = Settings()


# Ensure data directory exists
def ensure_data_directory():
    """Create data directory if it doesn't exist"""
    data_dir = Path(__file__).parent.parent.parent.parent / "data"
    data_dir.mkdir(exist_ok=True)
    return data_dir


ensure_data_directory()