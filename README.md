# MeteorCloud - Weather Forecast Application

## 📌 Overview
**MeteorCloud** is a Python-based web application that provides real-time weather forecasts for a given location. The application is designed with Object-Oriented Programming (OOP) principles, ensuring scalability, modularity, and ease of maintenance. It retrieves weather data from a third-party API and presents it in a user-friendly format.

## 🎯 Objectives
- Provide **accurate and up-to-date** weather forecasts for any location worldwide.
- Allow users to search for weather information using **city names, zip codes, or geographic coordinates**.
- Display **temperature, humidity, wind speed, and other weather details**.
- Support **unit conversions** between metric (Celsius, km/h) and imperial (Fahrenheit, mph).
- Implement **error handling** for incorrect inputs and API failures.
- Ensure extensibility for future enhancements such as multi-day forecasts and historical data analysis.

## 🚀 Features
### **Core Features:**
1. **User Input Handling**: Accepts location data in multiple formats:
   - Country, state, or city name
   - Zip/postal code
   - Geographic coordinates (latitude/longitude)
2. **Location-based Search**: Allows users to search for weather forecasts by entering any of the location parameters above.
3. **Weather Data Display**:
   - 🌡 **Temperature** (Celsius or Fahrenheit)
   - 💧 **Humidity** (%)
   - 🌬 **Wind Speed** (km/h or mph)
   - ☁️ **Weather Conditions** (Sunny, Rainy, Snowy, Cloudy, etc.)
   - 🧭 **Wind Direction** (North, South, East, West, etc.)
4. **Unit Conversion**: Toggle between metric (Celsius, km/h) and imperial (Fahrenheit, mph).
5. **Error Handling**: Manages invalid inputs (incorrect city names or coordinates), API errors (invalid API keys), and connectivity issues.

### **Advanced Features (Future Scope)**
- 🔔 **Weather Alerts**: Notifies users of extreme weather conditions.
- 📅 **Multi-day Forecasts**: Display weather forecasts for up to a week.
- 📊 **Historical Data Analysis**: Allows users to check past weather trends.
- 🌐 **Frontend Integration**: Develop a UI using HTML, CSS, and JavaScript.

---

## 📌 Technical Specifications
### **🖥️ Tech Stack**
| Component        | Technology Used  |
|-----------------|-----------------|
| **Programming Language** | Python 3.8+ |
| **Backend Framework** | Flask |
| **Database** | MongoDB |
| **Third-Party API** | OpenWeather API, Weather API |
| **Libraries** | `requests`, `json`, `datetime`, `pymongo`, `flask` |

### **🔧 Dependencies**
To install the required dependencies, use:
```bash
pip install flask requests pymongo
```

---

## 📌 Software Architecture
The application follows the **Model-View-Controller (MVC)** pattern:

1. **Weather API Class**
   - Fetches weather data from a third-party API.
   - Stores the API key and base URL.
   - Handles API requests and responses.

2. **Weather Data Class**
   - Stores and processes weather data fetched from the API.
   - Supports unit conversion (metric/imperial).

3. **Weather App Class**
   - Serves as the main application interface.
   - Handles user input and displays weather information.

```
MeteorCloud/
│── backend/                 # Backend source code
│   ├── app/                 # Main application package
│   │   ├── models/          # Database models
│   │   │   ├── weather.py   # Weather data model
│   │   │   ├── user.py      # User model (if needed)
│   │   │   ├── __init__.py  
│   │   ├── routes/          # API route handlers
│   │   │   ├── weather_routes.py  # Handles weather endpoints
│   │   │   ├── user_routes.py     # Handles user requests
│   │   │   ├── __init__.py  
│   │   ├── services/        # Business logic & external API calls
│   │   │   ├── weather_service.py  # Handles API integration (OpenWeather, etc.)
│   │   │   ├── location_service.py # Handles geolocation functionalities
│   │   │   ├── __init__.py  
│   │   ├── utils/           # Helper functions
│   │   │   ├── cache.py     # Caching mechanisms (Redis, in-memory)
│   │   │   ├── validators.py  # Input validation utilities
│   │   │   ├── __init__.py  
│   │   ├── config.py        # Application configuration settings
│   │   ├── database.py      # Database connection setup
│   │   ├── main.py          # Main entry point for the Flask app
│   │   ├── __init__.py  
│
│── frontend/                # Frontend source code
│   ├── static/              # Static assets (CSS, images, icons)
│   ├── templates/           # HTML templates for UI
│   ├── app.js               # JavaScript for frontend interactions
│   ├── index.html           # Main UI page
│
│── tests/                   # Unit and integration tests
│   ├── test_weather.py      # Test cases for weather features
│   ├── test_database.py     # Database-related tests
│   ├── __init__.py  
│
│── docs/                    # Documentation and API specs
│   ├── README.md            # Project overview
│   ├── API_REFERENCE.md     # API documentation
│   ├── INSTALLATION.md      # Setup and installation guide
│
│── scripts/                 # Deployment and maintenance scripts
│   ├── start_server.sh      # Shell script to start the server
│   ├── db_migrations.py     # Database migration scripts
│
│── .env                     # Environment variables (API keys, DB credentials)
│── .gitignore               # Git ignore file
│── requirements.txt         # Python dependencies
│── Dockerfile               # Dockerfile for containerization
│── docker-compose.yml       # Docker Compose configuration
│── manage.py                # Entry point for application management (if needed)
```
## 📌 Database Design
MeteorCloud uses **MongoDB** for storing weather data and user queries.

### **📂 Collections**
| Collection | Description |
|------------|-------------|
| `locations` | Stores user-provided locations with coordinates. |
| `weather_data` | Stores weather data fetched from the API. |
| `user_queries` | Logs user requests for tracking and analytics. |

### **📜 Sample MongoDB Document Structure**
#### **Weather Data Example:**
```json
{
  "location": "Uyo, Nigeria",
  "coordinates": {"lat": 5.0389, "lon": 7.9196},
  "temperature": {"celsius": 28, "fahrenheit": 82},
  "humidity": 80,
  "wind_speed": {"kmh": 15, "mph": 9},
  "weather_condition": "Cloudy",
  "timestamp": "2025-03-19T12:00:00Z"
}
```

---

## 📌 API Endpoints
| Endpoint | Method | Description |
|----------|--------|-------------|
| `/weather?location=<city_name>` | `GET` | Fetch real-time weather data for a given city. |
| `/weather?lat=<latitude>&lon=<longitude>` | `GET` | Fetch weather by GPS coordinates. |
| `/forecast?location=<city_name>` | `GET` | Fetch a 5-day weather forecast. |
| `/history?location=<city_name>` | `GET` | Retrieve past weather data. |
| `/unit-toggle?unit=<metric/imperial>` | `POST` | Toggle between metric and imperial units. |
| `/save-location` | `POST` | Save a user's preferred location. |
| `/delete-record?id=<record_id>` | `DELETE` | Delete a stored weather record. |

---

## 📌 Workflow
1. **User opens the application.**
2. **Application prompts for location input** (city, zip, coordinates, etc.).
3. **Weather API fetches weather data** based on user input.
4. **Weather Data class processes the data**, converting units if necessary.
5. **Weather App displays the weather information** to the user.
6. **User can save locations or toggle unit preferences.**
7. **Advanced Features (forecast, history, alerts) are available as needed.**

---

## 📌 Error Handling
- **Invalid Location**: If an incorrect city name is entered, the system suggests correct alternatives.
- **API Failure**: If the API is down, the system provides cached or default weather data.
- **Database Errors**: If MongoDB is unreachable, an error message is logged and displayed.
- **Rate Limiting**: If the API rate limit is exceeded, the system retries after a set period.

---

## 📌 Security Measures
- **API Key Protection**: API keys are stored securely in environment variables.
- **Input Validation**: User input is sanitized to prevent SQL injections and other attacks.
- **Data Encryption**: Sensitive user preferences are encrypted before storage.
- **Rate Limiting**: Restricts excessive API calls from a single IP.

---

## 📌 Deployment Guide
### **🚀 Running Locally**
1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/meteorcloud.git
   cd meteorcloud
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up environment variables in `.env` file:
   ```ini
   API_KEY=your_openweather_api_key
   MONGO_URI=mongodb://localhost:27017/meteorcloud
   ```
4. Run the Flask app:
   ```bash
   python app.py
   ```

### **🚀 Deploying to Production**
- Use **Gunicorn** and **NGINX** for serving the Flask application.
- Deploy to **AWS, Google Cloud, or Heroku** with a MongoDB Atlas backend.

---

## 📌 Conclusion
MeteorCloud is a **scalable, modular, and efficient** weather forecasting application designed with **best practices in API integration, database management, and error handling**. With potential future enhancements like **historical weather analysis and AI-based predictions**, the application is built for long-term extensibility.

**Contributors:** Victor Asuquo, Byron Itina, Diamond Umoh, Aniebietabasi Ime, Emmanuel, Chukwudi Valentine.

