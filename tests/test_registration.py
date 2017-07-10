"""
This module defines a class RegistrationTest that is used
to test the registration functionality.
"""
import unittest
from application.main import app

class RegistrationTest(unittest.TestCase):
    """
    Class to test registration of users into the application.
    """
    def setUp(self):
        self.app = app.test_client()
        
    def tearDown(self):
        self.app = None
    
    def test_registration_view_returns_200_status_code(self):
        """
        Return a status code of 200.
        """
        response = self.app.get('/register')
        self.assertEqual(response.status_code, 200, 
        "a status code of 200 should be sent as a response code")
        
    def test_register_renders_template(self):
        """
        Assert a string 'Register' is in data.
        """
        response = self.app.get('/register')
        self.assertIn(b'Register', response.data)
    
