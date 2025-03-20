import os
from pathlib import Path
import sys

# Add the root directory to Python path
ROOT_DIR = Path(__file__).parent.parent.parent.parent
sys.path.append(str(ROOT_DIR))

from backend.app.database import database

class Weather:
    def __init__(self, city, temperature, condition, timestamp):
        self.city = city
        self.temperature = temperature
        self.condition = condition
        self.timestamp = timestamp

    def save(self):
        collection = database.get_collection("weather")
        collection.insert_one(self.__dict__)

    @staticmethod
    def find_by_city(city):
        collection = database.get_collection("weather")
        return collection.find_one({"city": city})

    def __repr__(self):
        return f"Weather(city='{self.city}', temperature={self.temperature}, condition='{self.condition}')"