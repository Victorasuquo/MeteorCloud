import requests

def get_weather(city_name, units="metric"):
    """
    Fetch weather data for a given city using OpenWeatherMap API.
    
    Args:
        city_name (str): Name of the city.
        api_key (str): Your OpenWeatherMap API key.
        units (str): Units of measurement ('metric' for °C, 'imperial' for °F, 'standard' for K).
    
    Returns:
        dict: Weather details or error message.
    """
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city_name,
        "appid": "",
        "units": units  # 'metric' for Celsius, 'imperial' for Fahrenheit, 'standard' for Kelvin
    }
    
    try:
        response = requests.get(base_url, params=params)
        data = response.json()
        print(data)

        if response.status_code == 200:
            weather_info = {
            "City": data["name"],
            "Country": data["sys"]["country"],
            "Coordinates": f"Lat: {data['coord']['lat']}, Lon: {data['coord']['lon']}",
            "Temperature": f"{data['main']['temp']}°{'C' if units == 'metric' else 'F' if units == 'imperial' else 'K'}",
            "Feels Like": f"{data['main']['feels_like']}°{'C' if units == 'metric' else 'F' if units == 'imperial' else 'K'}",
            "Min Temperature": f"{data['main']['temp_min']}°{'C' if units == 'metric' else 'F' if units == 'imperial' else 'K'}",
            "Max Temperature": f"{data['main']['temp_max']}°{'C' if units == 'metric' else 'F' if units == 'imperial' else 'K'}",
            "Pressure": f"{data['main']['pressure']} hPa",
            "Humidity": f"{data['main']['humidity']}%",
            "Visibility": f"{data['visibility']} meters",
            "Wind Speed": f"{data['wind']['speed']} {'m/s' if units == 'metric' else 'mph'}",
            "Wind Direction": f"{data['wind']['deg']}°",
            "Wind Gust": f"{data['wind'].get('gust', 'N/A')} {'m/s' if units == 'metric' else 'mph'}",
            "Weather": data["weather"][0]["description"].capitalize(),
            "Cloudiness": f"{data['clouds']['all']}%",
            "Rain Volume (last 1h)": f"{data.get('rain', {}).get('1h', '0')} mm",
            "Sunrise": data["sys"]["sunrise"],
            "Sunset": data["sys"]["sunset"],
            "Timezone": data["timezone"],
            }
            return weather_info
        else:
            return {"Error": data.get("message", "Unable to fetch weather data")}
    except requests.exceptions.RequestException as e:
        return {"Error": str(e)}

# Example Usage
if __name__ == "__main__":
    city = "uyo"

    
    weather_data = get_weather(city)
    
    print("\nWeather Information:")
    for key, value in weather_data.items():
        print(f"{key}: {value}")
