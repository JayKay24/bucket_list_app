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
        
    def test_load_user_returns_False_if_user_does_not_exist(self):
        """
        Assert response is False if user does not exist.
        """
        response = self.bucket_list_app.load_user("winnie@gmail.com", "adisa")
        self.assertFalse(response, 
        "should return False if user is not registered")
        
    def test_create_bucketlist_returns_True_for_unique_bucketlist(self):
        """
        Assert response is True if bucketlist is unique.
        """
        self.bucket_list_app.load_user("james@gmail.com", "pass")
        response = self.bucket_list_app.create_bucketlist("Mountain Climbing", 
                                        "Climb all mountains in Kenya")
        self.assertTrue(response, 
        "should return True for a unique bucketlist entry")
        
    def test_delete_bucketlist_returns_False_if_bucketlist_does_not_exist(self):
        """
        Assert response is False if bucketlist does not exist.
        """
        self.bucket_list_app.load_user("james@gmail.com", "pass")
        response = self.bucket_list_app.delete_bucketlist("Mountain Climbing",
                                        "Climb all mountains in Kenya")
        self.assertFalse(response, 
        "should return False for a non-existent bucketlist")
        
    def test_delete_bucketlist_returns_True_if_bucketlist_exists(self):
        """
        Assert response is True if bucketlist exists for deleting.
        """
        self.bucket_list_app.load_user("james@gmail.com", "pass")
        self.bucket_list_app.create_bucketlist("Mountain Climbing", 
                                        "Climb all mountains in Kenya")
        response = self.bucket_list_app.delete_bucketlist("Mountain Climbing",
                                        "Climb all mountains in Kenya")
        self.assertTrue(response, "should return True if bucketlist exists")
        
    def test_edit_bucketlist_returns_True_if_bucketlist_exists(self):
        """
        Assert response is True if bucketlist exists for editing.
        """
        self.bucket_list_app.load_user("james@gmail.com", "pass")
        self.bucket_list_app.create_bucketlist("Mountain Climbing", 
                                        "Climb all mountains in Kenya")
        self.bucket_list_app.load_bucketlist("Mountain Climbing", 
                                        "Climb all mountains in Kenya")
        response = self.bucket_list_app.edit_bucketlist("Mountain Climbing", 
                                                        "Just Mount Kenya")
        self.assertTrue(response, 
        "should return True if bucketlist has beed edited")
    
    def test_create_bucketlist_item_returns_True_if_item_does_not_exist(self):
        """
        Assert response is True if bucketlist item does not exist.
        """
        self.bucket_list_app.load_user("james@gmail.com", "pass")
        self.bucket_list_app.create_bucketlist("Mountain Climbing", 
                                        "Climb all mountains in Kenya")
        self.bucket_list_app.load_bucketlist("Mountain Climbing", 
                                        "Climb all mountains in Kenya")
        response = self.bucket_list_app.create_bucketlist_item("Lenana", 
                                        "Climb Lenana peak and camp there.")
        self.assertTrue(response, 
        "should return True if a bucketlist item does not exist")