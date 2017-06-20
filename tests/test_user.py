import unittest
from application.classes.user import User

class UserTest(unittest.TestCase):
    def setUp(self):
        self.user = User('James', 'Kinyua')
    
    def test_user_id_is_none(self):
        self.assertIsNone(self.user.user_id, "user id should be none")
