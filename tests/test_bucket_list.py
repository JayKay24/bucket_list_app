"""
This module defines a test class for testing the BucketList class.
"""
import unittest

from application.models.bucket_list import BucketList

class BucketListTest(unittest.TestCase):
    def setUp(self):
        self.bucket_list = BucketList("Mountain climbing", 
        "Climb all mountains")
    
    def test_bucket_list_has_correct_name_and_description(self):
        self.assertEqual("Mountain climbing", self.bucket_list.name)
        