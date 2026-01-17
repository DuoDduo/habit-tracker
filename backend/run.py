"""
Entry point to run the Flask application
Author: Blessing Oluwapelumi James
Matric No: 92134091
"""

from app.main import create_app
from app.core.config import settings
from flasgger import Swagger  # 1. Import Swagger

app = create_app()
Swagger(app) # 2. Initialize Swagger with default settings

if __name__ == "__main__":
    print("=" * 60)
    print("Starting Habit Tracker API Server")
    print("=" * 60)
    print(f"Server running at: http://{settings.HOST}:{settings.PORT}")
    print(f"Swagger UI at: http://{settings.HOST}:{settings.PORT}/apidocs") # Added for easy access
    print(f" Database: {settings.DATABASE_URL}")
    print(f"Environment: {settings.FLASK_ENV}")
    print("=" * 60)
    
    app.run(
        host=settings.HOST,
        port=settings.PORT,
        debug=settings.FLASK_DEBUG
    )