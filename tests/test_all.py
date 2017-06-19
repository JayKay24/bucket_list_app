import unittest
from .bucket_tests import BucketlistTestResponse

def suite():
    """
    Return a composite testsuite.
    """
    
    response_suite = unittest.makeSuite(BucketlistTestResponse)
    
    return unittest.TestSuite((response_suite,))
    
if __name__ == '__main__':
    unittest.main(defaultTest='suite')