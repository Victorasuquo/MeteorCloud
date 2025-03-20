import unittest
from flask import Flask
import json
from backend.app.routes.user_routes import user_bp

class TestUserRoutes(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.app.register_blueprint(user_bp)
        self.client = self.app.test_client()

    def test_register_invalid_password(self):
        response = self.client.post('/register',
            json={"username": "testuser", "password": "weak"})
        self.assertEqual(response.status_code, 400)
        
    def test_register_valid_user(self):
        response = self.client.post('/register',
            json={"username": "testuser", "password": "StrongPass123!"})
        self.assertEqual(response.status_code, 201)

if __name__ == '__main__':
    unittest.main()