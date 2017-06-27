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
            if (user.email == email and user.password == password or
            user.fname == fname and user.lname == lname):
                return False
        user = User(fname, lname, email, password)
        self.users.append(user)
        return True
        
    def load_user(self, email, password):
        """
        Load the current user into the application upon logging in.
        """
        value = None
        for i in range(len(self.users)):
            if (self.users[i].email == email and 
            self.users[i].password == password):
                self.current_user = self.users.pop(i)
                value = True
                break
        else:
            value = False
        return value
        
    def create_bucketlist(self, name, description):
        """
        Create a bucketlist using the strings name and description.
        """
        if self.current_user is not None:
            for i in range(len(self.current_user.bucketlists)):
                if (self.current_user.bucketlists[i].name == name and 
                self.current_user.bucketlists[i].description == description):
                    return False
            # The bucketlist is unique.
            bucketlist = BucketList(name, description, self.current_user)
            self.current_user.bucketlists.append(bucketlist)
            return True
        else:
            return None
        
    def delete_bucketlist(self, name, description):
        """
        Delete a bucketlist using the strings name and description.
        """
        if self.current_user is not None:
            for i in range(len(self.current_user.bucketlists)):
                if (self.current_user.bucketlists[i].name == name and 
                self.current_user.bucketlists[i].description == description):
                    del self.current_user.bucketlists[i]
                    return True
            else:
                # The bucketlist was not found.
                return False
        else:
            return None
            
    def load_bucketlist(self, name, description):
        """
        Load the current bucketlist for editing.
        """
        if self.current_user is not None:
            for i in range(len(self.current_user.bucketlists)):
                if (self.current_user.bucketlists[i].name == name and 
                self.current_user.bucketlists[i].description == description):
                    self.current_bucketlist = self.current_user.bucketlists.pop(i)
                    return True
            else:
                return False
        else:
            return None
            
    def edit_bucketlist(self, name, description):
        """
        Edit a Bucketlist using the strings name and description.
        """
        if self.current_user is not None:
            if self.current_bucketlist is not None:
                self.current_bucketlist.name = name
                self.current_bucketlist.description = description
                self.current_user.bucketlists.append(self.current_bucketlist)
                return True
            else:
                return False
        else:
            return None
            
    def create_bucketlist_item(self, name, description):
        """
        Create a bucketlist item using the strings name and description.
        """
        if self.current_user is not None:
            if self.current_bucketlist is not None:
                for i in range(len(self.current_bucketlist.bucketlist_items)):
                    if (self.current_bucketlist.bucketlist_items[i].name == name
                    and self.current_bucketlist.bucketlist_items[i].description == description):
                        return False
                bucketlist_item = BucketListItem(name, description, 
                                                 self.current_bucketlist)
                self.current_bucketlist.bucketlist_items.append(bucketlist_item)
                return True
        else:
            return None
            
    def delete_bucketlist_item(self, name, description):
        """
        Delete a bucketlist item using the strings name and description.
        """
        if self.current_user is not None:
            if self.current_bucketlist is not None:
                for i in range(len(self.current_bucketlist.bucketlist_items)):
                    if (self.current_bucketlist.bucketlist_items[i].name == name
                    and self.current_bucketlist.bucketlist_items[i].description == description):
                        return True
                else:
                    return False
        else:
            return None

