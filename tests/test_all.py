import unittest
from homepage_tests import HomepageTest

def suite():
    """
    Return a composite testsuite.
    """
    
    home_suite = unittest.makeSuite(HomepageTest)
    
    return unittest.TestSuite((home_suite,))
    
if __name__ == '__main__':
    unittest.main(defaultTest='suite')