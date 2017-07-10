"""
This module defines a test suite for testing all the classes in the application.
"""
import unittest
from homepage_tests import HomepageTest
from test_user import UserTest
from test_bucket_list import BucketListTest
from test_login import LoginTest
from test_create_bucketlist import CreateBucketListTest
from test_bucket_list_app import BucketListAppTest

def suite():
    """
    Return a composite testsuite.
    """
    
    home_suite = unittest.makeSuite(HomepageTest)
    user_suite = unittest.makeSuite(UserTest)
    bucket_list_suite = unittest.makeSuite(BucketListTest)
    login_suite = unittest.makeSuite(LoginTest)
    create_bucketlist_suite = unittest.makeSuite(CreateBucketListTest)
    bucket_list_app_suite = unittest.makeSuite(BucketListAppTest)
    
    return unittest.TestSuite((home_suite, user_suite, bucket_list_suite, 
                               login_suite, create_bucketlist_suite,
                               bucket_list_app_suite))
    
if __name__ == '__main__':
    unittest.main(defaultTest='suite')
    