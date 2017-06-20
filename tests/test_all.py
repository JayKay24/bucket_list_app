import unittest
from homepage_tests import HomepageTest
from test_user import UserTest
from test_bucket_list import BucketListTest

def suite():
    """
    Return a composite testsuite.
    """
    
    home_suite = unittest.makeSuite(HomepageTest)
    user_suite = unittest.makeSuite(UserTest)
    bucket_list_suite = unittest.makeSuite(BucketListTest)
    
    return unittest.TestSuite((home_suite, user_suite, bucket_list_suite))
    
if __name__ == '__main__':
    unittest.main(defaultTest='suite')