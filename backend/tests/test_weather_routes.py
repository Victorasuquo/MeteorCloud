import unittest
from flask import Flask
from backend.app.routes.weather_routes import weather_bp

class TestWeatherRoutes(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.app.register_blueprint(weather_bp)
        self.client = self.app.test_client()

    def test_get_weather_no_city(self):
        response = self.client.get('/weather')
        self.assertEqual(response.status_code, 400)
        
    def test_get_weather_invalid_units(self):
        response = self.client.get('/weather?city=London&units=invalid')
        self.assertEqual(response.status_code, 400)

if __name__ == '__main__':
    unittest.main()