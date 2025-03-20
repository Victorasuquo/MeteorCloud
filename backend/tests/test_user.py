import unittest
from backend.app.models.user import User

class TestUser(unittest.TestCase):
    def test_password_verification(self):
        user = User("testuser", "password123")
        self.assertTrue(user.verify_password("password123"))
        self.assertFalse(user.verify_password("wrongpassword"))

if __name__ == '__main__':
    unittest.main()