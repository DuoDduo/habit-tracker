"""
Configuration Management
Author: Blessing Oluwapelumi James
Matric No: 92134091
"""

from pydantic_settings import BaseSettings
from typing import List
from pathlib import Path


class Settings(BaseSettings):
    """
    Application settings loaded from environment variables.
    Uses Pydantic for validation and type safety.
    """
    
    # Database
    # Using a relative path that works from the backend root
    DATABASE_URL: str = "sqlite:///./data/habits.db"
    
    # Flask
    FLASK_ENV: str = "development"
    FLASK_DEBUG: bool = True
    SECRET_KEY: str = "dev-secret-key-change-in-production"
    
    # Server
    HOST: str = "0.0.0.0"
    PORT: int = 5000
    
    # CORS
    CORS_ORIGINS: List[str] = ["http://localhost:3000", "http://localhost:8000"]
    
    class Config:
        env_file = ".env"
        case_sensitive = True
        # CRITICAL: Ignore extra fields (like VITE_ variables) in the .env file
        extra = "ignore"


# Global settings instance
settings = Settings()


def ensure_data_directory():
    """
    Create data directory if it doesn't exist.
    Calculates root path relative to this file's location:
    app/core/config.py -> app/core -> app -> root
    """
    # Go up 3 levels to reach the project root (backend/)
    base_dir = Path(__file__).resolve().parent.parent.parent
    data_dir = base_dir / "data"
    
    if not data_dir.exists():
        data_dir.mkdir(parents=True, exist_ok=True)
        print(f"Created data directory at: {data_dir}")
    
    return data_dir


# Initialize the directory on module load
ensure_data_directory()