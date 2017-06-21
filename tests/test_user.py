"""
This module instantiates and tests a User object.
"""
import unittest
from application.models.user import User

class UserTest(unittest.TestCase):
    def setUp(self):
        self.user = User('James', 'Kinyua', 'jameskinyua@gmail.com', 'jim')
    
    def test_user_id_is_none(self):
        """
        Assert that the initial user_id is None.
        """
        self.assertIsNone(self.user.user_id, "user id should be none")
    
    def test_password_is_correct(self):
        """
        Assert that the password is correct.
        """
        self.assertEqual(self.user.password, "jim")