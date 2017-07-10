"""
This module defines a class LoginTest to test the login view function.
"""
import unittest
from application.bucket_list_app import BucketListApp
from application.main import app

class LoginTest(unittest.TestCase):
    """
    Class to instantiate a LoginTest object which tests login/logout
    functionality.
    """
    def setUp(self):
        self.app = app.test_client()
        
    def tearDown(self):
        self.app = None
        
    def test_login_view_returns_200_status_code(self):
        """
        Assert that the response status code returns 200.
        """
        response = self.app.get('/login')
        self.assertEqual(response.status_code, 200, 
        "should return a status code of 200")
        
    def logout(self):
        """
        Helper method to log out the user.
        """
        return self.app.get('/logout', follow_redirects=True)
        