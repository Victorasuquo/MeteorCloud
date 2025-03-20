import requests
from typing import Optional, Dict
import logging

logger = logging.getLogger(__name__)

class WeatherService:
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
    API_KEY = "15a3c2be59942b8ad27a56231a0eb9a7"  # Move to config

    @staticmethod
    def get_weather(lat: float, lon: float, units: str = "metric", lang: str = "en") -> Optional[Dict]:
        """
        Get weather data for given coordinates
        
        Args:
            lat (float): Latitude
            lon (float): Longitude
            units (str): Units of measurement (metric/imperial/standard)
            lang (str): Language code
            
        Returns:
            Optional[Dict]: Weather data or None if request fails
        """
        try:
            params = {
                "lat": lat,
                "lon": lon,
                "appid": WeatherService.API_KEY,
                "units": units,
                "lang": lang
            }
            
            response = requests.get(
                WeatherService.BASE_URL,
                params=params,
                timeout=10
            )
            
            response.raise_for_status()
            data = response.json()
            
            return {
                "temperature": f"{data['main']['temp']}°{'C' if units == 'metric' else 'F'}",
                "feels_like": f"{data['main']['feels_like']}°{'C' if units == 'metric' else 'F'}",
                "humidity": f"{data['main']['humidity']}%",
                "description": data['weather'][0]['description'],
                "wind_speed": f"{data['wind']['speed']} {'m/s' if units == 'metric' else 'mph'}",
                "city_name": data['name'],
                "country": data['sys']['country']
            }
            
        except requests.RequestException as e:
            logger.error(f"API request failed: {str(e)}")
            return None
        except KeyError as e:
            logger.error(f"Invalid response format: {str(e)}")
            return None
        except Exception as e:
            logger.error(f"Unexpected error: {str(e)}")
            return None