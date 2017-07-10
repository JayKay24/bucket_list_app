"""
This module instantiates and tests a User object.
"""
import unittest
from application.models.user import User

class UserTest(unittest.TestCase):
    def setUp(self):
        self.user = User('James', 'Kinyua', 'jameskinyua@gmail.com', 'jim')
        
    def tearDown(self):
        self.user = None
    
    def test_password_is_correct(self):
        """
        Assert that the password is correct.
        """
        self.assertEqual(self.user.password, "jim")