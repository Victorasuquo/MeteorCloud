from pymongo import MongoClient
import os
from pathlib import Path
from typing import Optional

# Get the project root directory
ROOT_DIR = Path(__file__).parent.parent.parent
import sys
sys.path.append(str(ROOT_DIR))

from backend.app.config import config

class Database:
    def __init__(self):
        """Initialize the database connection."""
        self.client = MongoClient(config.MONGO_URI)
        self.db = self.client["MeteorCloudDB"]  # Explicitly define your database name

    def get_collection(self, name):
        """Retrieve a specific collection from the database."""
        return self.db[name]

# Create a global database instance
database = Database()
