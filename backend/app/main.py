from pathlib import Path
import sys
import logging
from flask import Flask
from flask_cors import CORS
from werkzeug.middleware.proxy_fix import ProxyFix

# Add the root directory to Python path
ROOT_DIR = Path(__file__).parent.parent.parent
sys.path.append(str(ROOT_DIR))

from backend.app.routes.weather_routes import weather_bp
from backend.app.routes.user_routes import user_bp
from backend.app.config import config

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def create_app():
    """Create and configure the Flask application"""
    app = Flask(__name__)
    
    # Configure app
    app.config['JSON_SORT_KEYS'] = False
    app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max-limit
    
    # Enable CORS
    CORS(app)
    
    # Fix for proxy headers
    app.wsgi_app = ProxyFix(app.wsgi_app)
    
    # Register blueprints
    app.register_blueprint(weather_bp, url_prefix="/api/v1")
    app.register_blueprint(user_bp, url_prefix="/api/v1")
    
    @app.errorhandler(404)
    def not_found(error):
        return {"error": "Resource not found", "status": "error"}, 404
        
    @app.errorhandler(500)
    def server_error(error):
        logger.error(f"Server error: {error}")
        return {"error": "Internal server error", "status": "error"}, 500
    
    return app

def main():
    """Main entry point for the application"""
    try:
        app = create_app()
        logger.info(f"Starting server in {config.ENV} mode")
        app.run(
            host="0.0.0.0",
            port=5000,
            debug=config.DEBUG
        )
    except Exception as e:
        logger.error(f"Failed to start server: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()