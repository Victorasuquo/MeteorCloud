from pathlib import Path
import sys
from flask import Blueprint, request, jsonify
from flask import current_app

from collections import defaultdict
from typing import Tuple, Dict, Any
import re
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


# Add the root directory to Python path
ROOT_DIR = Path(__file__).parent.parent.parent.parent
sys.path.append(str(ROOT_DIR))

from backend.app.models.user import User

user_bp = Blueprint("user", __name__)

def validate_password(password: str) -> bool:
    """
    Validate password strength
    - At least 8 characters
    - Contains uppercase and lowercase
    - Contains numbers
    - Contains special characters
    """
    if len(password) < 8:
        return False
    if not re.search(r"[A-Z]", password):
        return False
    if not re.search(r"[a-z]", password):
        return False
    if not re.search(r"\d", password):
        return False
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return False
    return True


@user_bp.route("/register", methods=["POST"])
def register() -> Tuple[Dict[str, Any], int]:
    """
    Register a new user
    
    Request Body:
        username (str): Username
        password (str): Password
        
    Returns:
        Tuple[Dict[str, Any], int]: Response data and HTTP status code
    """
    try:
        data = request.get_json()
        
        if not data:
            return jsonify({
                "error": "Invalid request body",
                "status": "error"
            }), 400
            
        username = data.get("username", "").strip()
        password = data.get("password", "")

        # Validate input
        if not username or not password:
            return jsonify({
                "error": "Username and password are required",
                "status": "error"
            }), 400
            
        if len(username) < 3:
            return jsonify({
                "error": "Username must be at least 3 characters",
                "status": "error"
            }), 400
            
        if not validate_password(password):
            return jsonify({
                "error": "Password must be at least 8 characters and contain uppercase, lowercase, numbers, and special characters",
                "status": "error"
            }), 400

        # Check if user exists
        if User.find_by_username(username):
            return jsonify({
                "error": "Username already exists",
                "status": "error"
            }), 409

        # Create and save user
        user = User(username, password)
        if user.save():
            return jsonify({
                "message": "User registered successfully",
                "username": username,
                "status": "success"
            }), 201
            
        return jsonify({
            "error": "Failed to create user",
            "status": "error"
        }), 500
        
    except Exception as e:
        logging.error(f"Registration error: {str(e)}")
        return jsonify({
            "error": "Internal server error",
            "status": "error"
        }), 500

# Add login route
@user_bp.route("/login", methods=["POST"])
def login() -> Tuple[Dict[str, Any], int]:
    """Handle user login"""
    try:
        data = request.get_json()
        
        username = data.get("username", "").strip()
        password = data.get("password", "")
        
        if not username or not password:
            return jsonify({
                "error": "Username and password are required",
                "status": "error"
            }), 400
            
        user = User.find_by_username(username)
        if not user or not User.verify_password(password):
            return jsonify({
                "error": "Invalid username or password",
                "status": "error"
            }), 401
            
        return jsonify({
            "message": "Login successful",
            "username": username,
            "status": "success"
        }), 200
        
    except Exception as e:
        logging.error(f"Login error: {str(e)}")
        return jsonify({
            "error": "Internal server error",
            "status": "error"
        }), 500
    

@user_bp.route("/routes", methods=["GET"])
def list_routes() -> Tuple[Dict[str, Any], int]:
    """
    List all registered routes in the application, grouped by module
    """
    try:
        # Group routes by their module
        route_groups = defaultdict(list)
        
        for rule in current_app.url_map.iter_rules():
            if rule.endpoint != 'static':  # Skip static file handling
                module = rule.endpoint.split('.')[0] if '.' in rule.endpoint else 'misc'
                route_groups[module].append({
                    "endpoint": rule.endpoint,
                    "methods": sorted(list(rule.methods - {'OPTIONS', 'HEAD'})),  # Remove default methods
                    "path": str(rule),
                    "description": current_app.view_functions[rule.endpoint].__doc__
                })

        # Format response
        formatted_routes = {
            module: sorted(routes, key=lambda x: x['path']) 
            for module, routes in route_groups.items()
        }
        
        logger.info(f"Retrieved routes from {len(route_groups)} modules")
        return jsonify({
            "routes": formatted_routes,
            "total_routes": sum(len(routes) for routes in route_groups.values()),
            "status": "success"
        }), 200
        
    except Exception as e:
        logger.error(f"Error listing routes: {str(e)}")
        return jsonify({
            "error": "Failed to list routes",
            "status": "error"
        }), 500