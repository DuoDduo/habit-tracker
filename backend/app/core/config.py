"""
Configuration Management
Author: Blessing Oluwapelumi James
Matric No: 92134091
"""

from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import List
from pathlib import Path
# ConfigDict is not needed for settings configuration


class Settings(BaseSettings):
    """
    Application settings loaded from environment variables.
    Uses Pydantic for validation and type safety.
    Attributes:
        DATABASE_URL: Database connection string
        FLASK_ENV: Flask environment (development/production)
        FLASK_DEBUG: Enable debug mode
        HOST: Server host address
        PORT: Server port number
        CORS_ORIGINS: Allowed CORS origins
    """
    
    # Database configuration
    # Using a relative path that works from the backend root
    DATABASE_URL: str = "sqlite:///./data/habits.db"
    
    # Flask configuration
    FLASK_ENV: str = "development"
    FLASK_DEBUG: bool = True
    
    # Server configuration
    HOST: str = "0.0.0.0"
    PORT: int = 5000
    
    # CORS
    CORS_ORIGINS: List[str] = ["http://localhost:3000", "http://localhost:8000", "http://127.0.0.1:3000",
        "http://127.0.0.1:8000"]
    
    # use the dedicated SettingsConfigDict type for environment settings
    model_config: SettingsConfigDict = SettingsConfigDict(
        env_file=".env",
        case_sensitive=True,
        extra="ignore",  # ignore unexpected fields
    )

# Global settings instance
settings = Settings()


def ensure_data_directory():
    """
    Create data directory if it doesn't exist.
    Calculates root path relative to this file's location:
    app/core/config.py -> app/core -> app -> root
      
    Returns:
        Path to data directory
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