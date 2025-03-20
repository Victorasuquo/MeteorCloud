from typing import Optional, Dict
import requests
from time import sleep
from urllib.parse import quote

class LocationService:
    """Service for handling geolocation requests"""
    
    GEO_API_URL = "https://nominatim.openstreetmap.org/search"
    USER_AGENT = "MeteorCloud/1.0"  # Required by Nominatim ToS
    
    @staticmethod
    def get_coordinates(city: str) -> Optional[Dict[str, float]]:
        """
        Get coordinates for a given city name
        
        Args:
            city (str): Name of the city to geocode
            
        Returns:
            Optional[Dict[str, float]]: Dictionary with lat/lon or None if not found
        """
        try:
            # Encode city name for URL
            encoded_city = quote(city)
            
            # Required headers for Nominatim
            headers = {
                'User-Agent': LocationService.USER_AGENT
            }
            
            params = {
                "q": encoded_city,
                "format": "json",
                "limit": 1
            }
            
            response = requests.get(
                LocationService.GEO_API_URL,
                params=params,
                headers=headers,
                timeout=10
            )
            
            response.raise_for_status()
            data = response.json()
            
            if data:
                return {
                    "lat": float(data[0]["lat"]),
                    "lon": float(data[0]["lon"]),
                    "display_name": data[0]["display_name"]
                }
            return None
            
        except requests.RequestException as e:
            print(f"API request failed: {e}")
            return None
        except (KeyError, IndexError) as e:
            print(f"Invalid response format: {e}")
            return None
        except Exception as e:
            print(f"Unexpected error: {e}")
            return None
        finally:
            # Rate limiting - Nominatim requires 1 second between requests
            sleep(1)