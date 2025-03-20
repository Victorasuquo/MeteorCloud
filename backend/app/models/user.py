import os
from pathlib import Path
import sys
import hashlib
import secrets
from typing import Optional, Dict
from datetime import datetime

# Add the root directory to Python path
ROOT_DIR = Path(__file__).parent.parent.parent.parent
sys.path.append(str(ROOT_DIR))

from backend.app.database import database

class User:
    def __init__(self, username: str, password: str):
        self.username = username
        self.salt = self._generate_salt()
        self.password = self._hash_password(password, self.salt)
        self.created_at = datetime.utcnow()
        self.updated_at = self.created_at
        self.active = True

    def save(self) -> bool:
        """Save user to database"""
        try:
            collection = database.get_collection("users")
            self.updated_at = datetime.utcnow()
            collection.insert_one(self.__dict__)
            return True
        except Exception as e:
            print(f"Error saving user: {e}")
            return False

    @staticmethod
    def find_by_username(username: str) -> Optional[Dict]:
        """Find user by username"""
        collection = database.get_collection("users")
        return collection.find_one({"username": username})

    def verify_password(self, password: str) -> bool:
        """Verify password against stored hash"""
        return self.password == self._hash_password(password, self.salt)

    @staticmethod
    def _generate_salt(length: int = 16) -> str:
        """Generate random salt for password hashing"""
        return secrets.token_hex(length)

    def _hash_password(self, password: str, salt: str) -> str:
        """Hash password with salt using SHA-256"""
        salted = password + salt
        return hashlib.sha256(salted.encode()).hexdigest()

    def __repr__(self) -> str:
        return f"User(username='{self.username}', created_at='{self.created_at}')"