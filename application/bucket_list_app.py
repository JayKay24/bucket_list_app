from app import app
from models.bucket_list import BucketList
from models.bucket_list_item import BucketListItem
from models.user import User

class BucketListApp:
    """
    Controller class to manipulate class models.
    """
    def __init__(self):
        self.users = []
        self.current_user = None
        self.current_bucketlist = None
        self.current_bucketlist_item = None
        
    def create_user(self, fname, lname, email, password):
        """
        Create a user upon registration.
        """
        for user in self.users:
            if (user.fname == fname and user.lname == lname):
                return False
        user = User(fname, lname, email, password)
        return True


