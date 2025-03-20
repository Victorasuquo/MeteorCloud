import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

class Config:
    # Environment settings
    ENV = os.getenv("FLASK_ENV", "development")
    DEBUG = os.getenv("DEBUG", "False").lower() == "true"
    
    # API settings
    WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")
    API_VERSION = "v1"
    
    # Database settings
    MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
    DB_NAME = os.getenv("DB_NAME", "meteorcloud")
    
    # Security settings
    SECRET_KEY = os.getenv("SECRET_KEY")
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")
    
    def validate(self):
        required_vars = ["WEATHER_API_KEY", "MONGO_URI", "SECRET_KEY"]
        missing = [var for var in required_vars if not getattr(self, var)]
        if missing:
            raise ValueError(f"Missing required configuration: {', '.join(missing)}")

config = Config()