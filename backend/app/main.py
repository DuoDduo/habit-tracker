"""
Flask Application Factory
Author: Blessing Oluwapelumi James
Matric No: 92134091
"""

from flask import Flask, jsonify
from flask_cors import CORS
from app.core.config import settings
from app.db.session import init_db
from app.api.endpoints.habits import habits_bp
from app.api.endpoints.analytics import analytics_bp


def create_app() -> Flask:
    """
    Application factory pattern.
    Creates and configures the Flask application.
    
    Returns:
        Configured Flask app instance
    """
    app = Flask(__name__)
    
    # Load configuration
    app.config["SECRET_KEY"] = settings.SECRET_KEY
    app.config["DEBUG"] = settings.FLASK_DEBUG
    
    # Enable CORS
    CORS(app, resources={
        r"/api/*": {
            "origins": settings.CORS_ORIGINS,
            "methods": ["GET", "POST", "DELETE", "OPTIONS"],
            "allow_headers": ["Content-Type"]
        }
    })
    
    # Initialize database
    init_db()
    
    # Register blueprints
    app.register_blueprint(habits_bp)
    app.register_blueprint(analytics_bp)
    
    # Health check endpoint
    @app.route("/")
    def index():
        return jsonify({
            "message": "Habit Tracker API",
            "version": "1.0.0",
            "author": "Blessing Oluwapelumi James",
            "matric_no": "92134091",
            "status": "running"
        })
    
    @app.route("/health")
    def health():
        return jsonify({"status": "healthy"}), 200
    
    # Error handlers
    @app.errorhandler(404)
    def not_found(error):
        return jsonify({"error": "Not found"}), 404
    
    @app.errorhandler(500)
    def internal_error(error):
        return jsonify({"error": "Internal server error"}), 500
    
    return app