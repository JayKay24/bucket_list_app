"""
This module contains tests for the homepage view function.
"""
import unittest
from application.main import app

class HomepageTest(unittest.TestCase):
    """
    Class to test response data from homepage view.
    """
    def setUp(self):
        self.app = app.test_client()
        
    def test_homepage_returns_200(self):
        """
        Return a status code of 200.
        """
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
    
    def test_homepage_renders_template(self):
        response = self.app.get('/')
        self.assertIn(b'Welcome to Bucket List Creator.', response.data)
        
if __name__ == '__main__':
    unittest.main()
    