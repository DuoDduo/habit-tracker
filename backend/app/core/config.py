"""
Configuration Management
Author: Blessing Oluwapelumi James
Matric No: 92134091
"""

# Import BaseSettings to automatically load environment variables into a class
# Import SettingsConfigDict to configure how environment variables are handled
from pydantic_settings import BaseSettings, SettingsConfigDict

# Import List type for type hinting (used for CORS origins)
from typing import List

# Import Path for cross-platform filesystem path handling
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
    # Default SQLite database path (relative to project root)
    # Can be overridden using environment variables
    DATABASE_URL: str = "sqlite:///./data/habits.db"
    
  
    # Flask configuration
    # Environment type (development or production)
    FLASK_ENV: str = "development"

    # Enable/disable Flask debug mode
    FLASK_DEBUG: bool = True
    

    # Server configuration
    # Host address the application binds to
    # 0.0.0.0 allows access from external devices (e.g., Docker or LAN)
    HOST: str = "0.0.0.0"

    # Port number the server runs on
    PORT: int = 5000
    

    # CORS configuration
    # List of allowed frontend origins for cross-origin requests
    # Important for browser security when frontend and backend run on different ports
    CORS_ORIGINS: List[str] = [
        "http://localhost:3000",
        "http://localhost:8000",
        "http://127.0.0.1:3000",
        "http://127.0.0.1:8000"
    ]
    

    # Pydantic model configuration
   
    # Use the dedicated SettingsConfigDict type for environment settings
    model_config: SettingsConfigDict = SettingsConfigDict(
        env_file=".env",          # Load environment variables from .env file
        case_sensitive=True,      # Variable names are case sensitive
        extra="ignore",           # Ignore unexpected environment variables
    )


# Global settings instance
# This creates a singleton-style configuration object
# Automatically loads values from environment variables at import time
settings = Settings()


def ensure_data_directory():
    """
    Create data directory if it doesn't exist.
    Calculates root path relative to this file's location:
    app/core/config.py -> app/core -> app -> root
      
    Returns:
        Path to data directory
    """
    # Resolve the absolute path of this file (config.py)
    # Then navigate up three directory levels to reach project root
    base_dir = Path(__file__).resolve().parent.parent.parent

    # Construct the path to the "data" directory inside project root
    data_dir = base_dir / "data"
    
    # Check whether the data directory already exists
    if not data_dir.exists():
        # Create the directory (including parent folders if needed)
        # exist_ok=True prevents error if directory was created concurrently
        data_dir.mkdir(parents=True, exist_ok=True)

        # Print confirmation (useful during development)
        print(f"Created data directory at: {data_dir}")
    
    # Return the Path object for further use if needed
    return data_dir


# Initialize the directory on module load
# This ensures the required data folder exists before the application starts
ensure_data_directory()