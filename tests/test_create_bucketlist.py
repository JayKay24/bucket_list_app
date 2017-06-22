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
        
    def create_a_bucketlist(self, name, description):
        """
        Create a bucketlist for the user.
        """
        return self.app.post('/create-bucketlist', 
            data=dict(name=name, description=description), 
            follow_redirects=True)
        
    def test_create_bucketlist_returns_success_message(self):
        """
        The success message should be rendered in the redirected page.
        """
        response = self.create_a_bucketlist("Mountain climbing", 
        "I wanna climb all mountains")
        assert b'Bucket List has been successfully created!' in response.data

