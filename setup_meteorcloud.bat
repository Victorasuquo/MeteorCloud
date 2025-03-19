@echo off
setlocal enabledelayedexpansion

:: Set project name
set PROJECT_NAME=MeteorCloud

:: Create main project directory
mkdir %PROJECT_NAME%
cd %PROJECT_NAME%

:: Create Backend structure
mkdir backend
cd backend
mkdir app
mkdir app\models
mkdir app\routes
mkdir app\services
mkdir app\utils
mkdir tests
mkdir docs
mkdir scripts
cd ..

:: Create Frontend structure
mkdir frontend
cd frontend
mkdir static
mkdir templates
cd ..

:: Create necessary files
cd backend\app
echo # Configuration settings > config.py
echo # Database connection setup > database.py
echo # Main FastAPI/Flask entry point > main.py
echo # Init file > __init__.py
cd models
echo # Weather data model > weather.py
echo # User model > user.py
echo # Init file > __init__.py
cd ..\routes
echo # Weather API routes > weather_routes.py
echo # User API routes > user_routes.py
echo # Init file > __init__.py
cd ..\services
echo # Weather service API calls > weather_service.py
echo # Geolocation service > location_service.py
echo # Init file > __init__.py
cd ..\utils
echo # Caching mechanisms > cache.py
echo # Input validation utilities > validators.py
echo # Init file > __init__.py
cd ..\..

:: Create test cases
cd tests
echo # Test cases for weather features > test_weather.py
echo # Database-related tests > test_database.py
echo # Init file > __init__.py
cd ..

:: Create documentation files
cd docs
echo # Project overview > README.md
echo # API Documentation > API_REFERENCE.md
echo # Installation guide > INSTALLATION.md
cd ..

:: Create frontend files
cd frontend
echo // Main frontend JavaScript > app.js
echo <!DOCTYPE html>^
<html>^
<head>^
    <title>MeteorCloud</title>^
</head>^
<body>^
    <h1>Welcome to MeteorCloud</h1>^
</body>^
</html> > index.html
cd ..

:: Create environment and deployment files
echo # Environment variables > .env
echo # Git ignore file > .gitignore
echo # Python dependencies > requirements.txt
echo # Dockerfile for containerization > Dockerfile
echo # Docker Compose configuration > docker-compose.yml
echo # App management script > manage.py

echo MeteorCloud project structure created successfully!
pause
