import unittest
from homepage_tests import HomepageTest
from test_user import UserTest

def suite():
    """
    Return a composite testsuite.
    """
    
    home_suite = unittest.makeSuite(HomepageTest)
    user_suite = unittest.makeSuite(UserTest)
    
    return unittest.TestSuite((home_suite, user_suite))
    
if __name__ == '__main__':
    unittest.main(defaultTest='suite')