from pathlib import Path
import sys
from flask import Blueprint, request, jsonify
from typing import Tuple, Dict, Any
import logging

# Configure logging
logger = logging.getLogger(__name__)

# Add the root directory to Python path
ROOT_DIR = Path(__file__).parent.parent.parent.parent
sys.path.append(str(ROOT_DIR))

from backend.app.services.weather_service import WeatherService
from backend.app.services.location_service import LocationService

weather_bp = Blueprint("weather", __name__)

@weather_bp.route("/weather", methods=["GET"])
def get_weather() -> Tuple[Dict[str, Any], int]:
    """
    Get current weather data for a city
    
    Query Parameters:
        city (str): Name of the city
        units (str, optional): Units of measurement (metric/imperial)
        lang (str, optional): Language code for weather descriptions
        
    Returns:
        Tuple[Dict[str, Any], int]: Weather data and HTTP status code
    """
    try:
        # Validate input parameters
        city = request.args.get("city", "").strip()
        units = request.args.get("units", "metric")
        lang = request.args.get("lang", "en")
        
        if not city:
            return jsonify({
                "error": "City parameter is required",
                "status": "error"
            }), 400
            
        if units not in ["metric", "imperial", "standard"]:
            return jsonify({
                "error": "Invalid units parameter. Use 'metric', 'imperial', or 'standard'",
                "status": "error"
            }), 400

        # Get coordinates for the city
        location = LocationService.get_coordinates(city)
        if not location:
            return jsonify({
                "error": f"Could not find coordinates for {city}",
                "status": "error"
            }), 404

        # Get weather data using coordinates
        weather = WeatherService.get_weather(
            lat=location["lat"],
            lon=location["lon"],
            units=units,
            lang=lang
        )
        
        if weather:
            return jsonify({
                "data": weather,
                "status": "success"
            }), 200
            
        return jsonify({
            "error": f"Weather data not found for {city}",
            "status": "error"
        }), 404
        
    except Exception as e:
        logger.error(f"Error getting weather data: {str(e)}")
        return jsonify({
            "error": "Failed to fetch weather data",
            "status": "error"
        }), 500