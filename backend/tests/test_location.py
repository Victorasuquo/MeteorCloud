import unittest
from unittest.mock import patch
from backend.app.services.location_service import LocationService

class TestLocationService(unittest.TestCase):
    @patch('requests.get')
    def test_get_coordinates(self, mock_get):
        # Mock successful API response
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = [{
            "lat": "51.5074",
            "lon": "-0.1278",
            "display_name": "London, Greater London, England, UK"
        }]

        result = LocationService.get_coordinates("London")
        
        self.assertIsNotNone(result)
        self.assertEqual(result["lat"], 51.5074)
        self.assertEqual(result["lon"], -0.1278)

if __name__ == '__main__':
    unittest.main()