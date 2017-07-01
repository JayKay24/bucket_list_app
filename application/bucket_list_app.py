from models.bucket_list import BucketList
from models.bucket_list_item import BucketListItem
from models.user import User


class BucketListApp:
    """
    Controller class to manipulate class models.
    """
    def __init__(self):
        self.users = {}
        
    def create_user(self, fname, lname, email, password):
        """
        Create a user upon registration.
        """
        if len(self.users) >=1:
            for name, user in self.users.items():
                if (email+password) == name:
                    return False
            # The user is unique.
            user = User(fname, lname, email, password)
            self.users[user.get_credentials] = user
        return True
        
    def load_user(self, email, password):
        """
        Load the current user into the application upon logging in.
        """
        for name, user in self.users.items():
            if (email+password) == user.get_credentials():
                user.current = True
                return True
        return False
        
    def return_user(self):
        """
        Reset the current attribute of User class to False.
        """
        for name, user in self.users.items():
            if user.current is True:
                user.current = False
        
    def create_bucketlist(self, name, description):
        """
        Create a bucketlist using the strings name and description.
        """
        for name, user in self.users.items():
            if user.current is True:
                for bucketlist_name, bucketlist in self.users.bucketlists.items():
                    if (name+description) == bucketlist_name:
                        return False
                user.bucketlists[name+description] = BucketList(name, 
                                                description)
                return True
        
    def delete_bucketlist(self, name, description):
        """
        Delete a bucketlist using the strings name and description.
        """
        for name, user in self.users.items():
            if user.current is True:
                for bucketlist_name, bucketlist in user.bucketlists.items():
                    if (name+description) == bucketlist_name:
                        user.bucketlists.pop(bucketlist_name, None)
                        return True
            
    def load_bucketlist(self, name, description):
        """
        Load the current bucketlist for editing.
        """
        for name, user in self.users.items():
            for bucketlist_name, bucketlist in user.bucketlists.items():
                if (name+description) == bucketlist_name:
                    bucketlist.current = True
            
    def return_bucketlist(self):
        """
        Reset the loaded bucketlist's current attribute to False.
        """
        for name, user in self.users.items():
            for bucketlist_name, bucketlist in user.bucketlists.items():
                if bucketlist.current is True:
                    bucketlist.current = False
            
    def edit_bucketlist(self, name, description):
        """
        Edit a Bucketlist using the strings name and description.
        """
        for name, user in self.users.items():
            if user.current is True:
                for bucketlist_name, bucketlist in user.bucketlists.items():
                    if bucketlist.current is True:
                        bucketlist.name = name
                        bucketlist.description = description
                        return True
                else:
                    return False
            
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
            
    def load_bucketlist_item(self, name, description):
        """
        Load the current bucketlist item for editing.
        """
        if self.current_user is not None:
            if self.current_bucketlist is not None:
                for i in range(len(self.current_bucketlist.bucketlist_items)):
                    if (self.current_bucketlist.bucketlist_items[i].name == name
                    and self.current_bucketlist.bucketlist_items[i].description == description):
                        self.current_bucketlist_item = self.current_bucketlist.bucketlist_items.pop(i)
                        return True
                else:
                    return False
        else:
            return None
            
    def return_bucketlist_item(self):
        """
        Append the loaded bucketlist item back into the current user's
        loaded bucketlist.
        """
        if self.current_user is not None:
            if self.create_bucketlist is not None:
                if self.current_bucketlist_item is not None:
                    self.current_bucketlist.bucketlist_items.append(
                            self.create_bucketlist_item)
                    self.current_bucketlist_item = None
                    return True
            else:
                return False
        else:
            return None
            
    def edit_bucketlist_item(self, name, description):
        """
        Edit a bucketlist using the strings name and description.
        """
        if self.current_user is not None:
            if self.current_bucketlist is not None:
                if self.current_bucketlist_item is not None:
                    self.current_bucketlist_item.name = name
                    self.current_bucketlist_item.description = description
                    self.current_bucketlist.bucketlist_items.append(self.current_bucketlist_item)
                    return True
                else:
                    return False
        else:
            return None

