import unittest
from application.classes.user import User

class UserTest(unittest.TestCase):
    def setUp(self):
        self.user = User('James', 'Kinyua', 'jameskinyua@gmail.com', 'jim')
    
    def test_user_id_is_none(self):
        self.assertIsNone(self.user.user_id, "user id should be none")
    
    def test_password_is_correct(self):
        self.assertEqual(self.user.password, "jim")