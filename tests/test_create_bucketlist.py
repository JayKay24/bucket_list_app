"""
This module defines a function CreateBucketListTest which tests for adding
a bucketlist item.
"""

import unittest

from application.main import app

class CreateBucketListTest(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        
    def tearDown(self):
        self.app = None
        
    def test_create_bucketlist_view_returns_200_status_code(self):
        """
        Assert that the response status code returns 200.
        """
        response = self.app.get('/create-bucketlist')
        self.assertEqual(response.status_code, 200, 
        "should return a status code of 200")
        
