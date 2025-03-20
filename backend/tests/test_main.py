import unittest
from backend.app.main import create_app

class TestMain(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()
        
    def test_not_found(self):
        response = self.client.get('/nonexistent')
        self.assertEqual(response.status_code, 404)
        
    def test_api_prefix(self):
        response = self.client.get('/api/v1/weather')
        self.assertNotEqual(response.status_code, 404)

if __name__ == '__main__':
    unittest.main()