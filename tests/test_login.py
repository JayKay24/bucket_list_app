"""
This module defines a class LoginTest to test the login view function.
"""
import unittest
from application.main import app

class LoginTest(unittest.TestCase):
    """
    Class to instantiate a LoginTest object which tests login/logout
    functionality.
    """
    def setUp(self):
        self.app = app.test_client()
        
    def login(self, email, password):
        """
        Helper method to log in the user.
        """
        return self.app.post('login', data=dict(
        email=email, password=password), follow_redirects=True)
        
    def logout(self):
        """
        Helper method to log out the user.
        """
        return self.app.get('/logout', follow_redirects=True)
        
    def test_login(self):
        """
        Assert login message is in homepage.
        """
        response = self.login('jameskinyua@gmail.com', 'admin')
        assert b'You have been successfully logged in!' in response.data
        
    def test_login_invalid_credentials(self):
        """
        Assert login returns registration message.
        """
        response = self.login('jimmy@gmail.com', 'admin')
        assert b'Please register with the application first' in response.data