"""
This module defines a test suite for testing all the classes in the application.
"""
import unittest
from homepage_tests import HomepageTest
from test_user import UserTest
from test_bucket_list import BucketListTest
from test_login import LoginTest

def suite():
    """
    Return a composite testsuite.
    """
    
    home_suite = unittest.makeSuite(HomepageTest)
    user_suite = unittest.makeSuite(UserTest)
    bucket_list_suite = unittest.makeSuite(BucketListTest)
    login_suite = unittest.makeSuite(LoginTest)
    
    return unittest.TestSuite((home_suite, user_suite, bucket_list_suite, 
                               login_suite))
    
if __name__ == '__main__':
    unittest.main(defaultTest='suite')
    