"""
Flask Application Factory
Author: Blessing Oluwapelumi James
Matric No: 92134091
Creates and configures the Flask application instance.
"""

# Import Flask core classes and utilities
from flask import Flask, jsonify

# CORS support for allowing frontend requests
from flask_cors import CORS

# Import global settings
from app.core.config import settings

# Import database initializer
from app.db.session import init_db

# Import API blueprints for registering endpoints
from app.api.endpoints.habits import habits_bp
from app.api.endpoints.analytics import analytics_bp


def create_app() -> Flask:
    """
    Application factory pattern.
    Creates and configures the Flask application.
    
    Returns:
        Configured Flask app instance
    """

    # Create Flask app instance
    app = Flask(__name__)
    
    # Load configuration from settings
    # Example: app.config["SECRET_KEY"] = settings.SECRET_KEY
    app.config["DEBUG"] = settings.FLASK_DEBUG  # Enable debug mode if set in config
    

    # Enable CORS for frontend integration
    # This ensures the frontend can make requests to /api/* endpoints
    CORS(app, resources={
        r"/api/*": {
            "origins": settings.CORS_ORIGINS,  # Allowed origins from config
            "methods": ["GET", "POST", "DELETE", "OPTIONS"],  # Allowed HTTP methods
            "allow_headers": ["Content-Type"]  # Allowed headers
        }
    })
    
    # Initialize database tables
    init_db()  # Creates tables if they do not exist yet
    
    # Register API blueprints
    # Each blueprint contains its own routes and handlers
    app.register_blueprint(habits_bp)
    app.register_blueprint(analytics_bp)
    

    # Root endpoint for API info
    @app.route("/")
    def index():
        """Root endpoint - API information"""
        return jsonify({
            "message": "Habit Tracker API",
            "version": "1.0.0",
            "author": "Blessing Oluwapelumi James",
            "matric_no": "92134091",
            "status": "running",
            "endpoints": {
                "habits": "/api/habits",
                "analytics": "/api/analytics"
            }
        })
    
    # Health check endpoint
    @app.route("/health")
    def health():
        """Health check endpoint"""
        return jsonify({"status": "healthy"}), 200
    

    # Error handlers
    
    @app.errorhandler(404)
    def not_found(error):
        """Handle 404 errors with JSON response"""
        return jsonify({"error": "Resource not found"}), 404
    
    @app.errorhandler(500)
    def internal_error(error):
        """Handle 500 errors with JSON response"""
        return jsonify({"error": "Internal server error"}), 500
    
    @app.errorhandler(400)
    def bad_request(error):
        """Handle 400 errors"""
        return jsonify({"error": "Bad request"}), 400
    
    # Return the configured app instance
    return app