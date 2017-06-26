"""
This module defines a class BucketListAppTest used to test the class 
BucketListApp
"""
import unittest

from application.models.bucket_list import BucketList
from application.models.bucket_list_item import BucketListItem
from application.models.user import User
from application.bucket_list_app import BucketListApp

class BucketListAppTest(unittest.TestCase):
    def setUp(self):
        self.bucket_list_app = BucketListApp()
        self.bucket_list_app.create_user("James", "Kinyua", "james@gmail.com",
                                         "pass")
        
    def tearDown(self):
        self.bucket_list_app = None
        
    def test_bucket_list_app_create_duplicate_user_returns_False(self):
        """
        Assert response is false for already registered user.
        """
        response = self.bucket_list_app.create_user("James", "Kinyua", 
        "james@gmail.com", "pass")
        self.assertFalse(response, 
        "should return False for already registered user")
        