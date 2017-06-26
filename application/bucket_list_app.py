from app import app
from models.bucket_list import BucketList
from models.bucket_list_item import BucketListItem
from models.user import User

all_users = []
all_bucketlists = []

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
            if (user.email == email and user.fname == fname and 
            user.lname == lname):
                return False
        user = User(fname, lname, email, password)
        self.users.append(user)
        return True
        
    def load_user(self, email, password):
        """
        Load the current user into the application upon logging in.
        """
        for i in range(len(self.users)):
            if (self.users[i].email == email and 
            self.users[i].password == password):
                self.current_user = self.users.pop(i)
                return True
        return False
        
    def create_bucketlist(self, name, description):
        """
        Create a bucketlist using the strings name and description.
        """
        if self.current_user is not None:
            for i in range(len(self.current_user.bucketlists)):
                if (self.current_user.bucketlists[i].name == name and 
                self.create_user.bucketlists[i].description == description):
                    return False
            # The bucketlist is unique.
            bucketlist = BucketList(name, description, self.current_user)
            self.current_user.bucketlists.append(bucketlist)
            return True
        else:
            return None
        


