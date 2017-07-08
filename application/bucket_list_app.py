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
            for username, user in self.users.items():
                if (email+password) == username:
                    return False
        # The user is unique.
        user = User(fname, lname, email, password)
        self.users[user.get_credentials()] = user
        return True
        
    def load_user(self, email, password):
        """
        Load the current user into the application upon logging in.
        """
        if len(self.users) > 0:
            self.return_user()
            for username, user in self.users.items():
                if (email+password) == username:
                    user.current = True
                    return True
            else:
                return False
        else:
            return False
        
    def return_user(self):
        """
        Reset the current attribute of User class to False.
        """
        for username, user in self.users.items():
            user.rename_bucketlist_keys()
            if user.current is True:
                user.current = False
                return True
        
    def create_bucketlist(self, name, description):
        """
        Create a bucketlist using the strings name and description.
        """
        for username, user in self.users.items():
            user.rename_bucketlist_keys()
            if user.current is True:
                for bucketlist_name, bucketlist in user.bucketlists.items():
                    if (name+description) == bucketlist_name:
                        return False
                user.bucketlists[name+description] = BucketList(name, 
                                                description)
                print(user.bucketlists)
                return True
        
    def delete_bucketlist(self, name, description):
        """
        Delete a bucketlist using the strings name and description.
        """
        for username, user in self.users.items():
            user.rename_bucketlist_keys()
            print(user.bucketlists)
            if user.current is True:
                for bucketlist_name, bucketlist in user.bucketlists.items():
                    print(bucketlist_name)
                    if (name+description) == bucketlist_name:
                        user.bucketlists.pop(bucketlist_name, None)
                        print(user.bucketlists)
                        return True
                else:
                    return False
            
    def load_bucketlist(self, name, description):
        """
        Load the current bucketlist for editing.
        """
        self.return_bucketlist()
        for username, user in self.users.items():
            user.rename_bucketlist_keys()
            for bucketlist_name, bucketlist in user.bucketlists.items():
                if (name+description) == bucketlist_name:
                    bucketlist.current = True
                    return True
            
    def return_bucketlist(self):
        """
        Reset the loaded bucketlist's current attribute to False.
        """
        for username, user in self.users.items():
            user.rename_bucketlist_keys()
            for bucketlist_name, bucketlist in user.bucketlists.items():
                if bucketlist.current is True:
                    bucketlist.current = False
                    return True
                    
    def rename_dictionary(self, a_dictionary):
        """
        Reset the keys of an arbitrary dictionary to new names.
        """
        all_values = a_dictionary.values()
        a_dictionary.clear()
        for value in all_values:
            a_dictionary[value.get_full_name()] = value
        return a_dictionary
            
    def edit_bucketlist(self, name, description):
        """
        Edit a Bucketlist using the strings name and description.
        """
        for username, user in self.users.items():
            user.rename_bucketlist_keys()
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
        for username, user in self.users.items():
            if user.current is True:
                for bucketlist_name, bucketlist in user.bucketlists.items():
                    bucketlist.rename_bucketlist_item_keys()
                    if bucketlist.current is True:
                        bucketlist_item = BucketListItem(name, description)
                        bucketlist.bucketlist_items[bucketlist_item.get_full_name()] = bucketlist_item
                        return True
                else:
                    return False
            
    def delete_bucketlist_item(self, name, description):
        """
        Delete a bucketlist item using the strings name and description.
        """
        for username, user in self.users.items():
            if user.current is True:
                for bucketlist_name, bucketlist in user.bucketlists.items():
                    bucketlist.rename_bucketlist_item_keys()
                    if bucketlist.current is True:
                        for bucketitem_name, bucketitem in bucketlist.bucketlist_items.items():
                            if (name+description) == bucketitem_name:
                                bucketlist.bucketlist_items.pop(bucketitem_name, None)
                                return True
                        else:
                            return False
        else:
            return None
            
    def load_bucketlist_item(self, name, description):
        """
        Load the current bucketlist item for editing.
        """
        self.return_bucketlist_item()
        for username, user in self.users.items():
            if user.current is True:
                for bucketlist_name, bucketlist in user.bucketlists.items():
                    bucketlist.rename_bucketlist_item_keys()
                    if bucketlist.current is True:
                        for bucketitem_name, bucketitem in bucketlist.bucketlist_items.items():
                            if (name+description) == bucketitem_name:
                                bucketitem.current = True
                                return True
        else:
            return None
            
    def return_bucketlist_item(self):
        """
        Reset the loaded bucketlist item's current attriibute to False.
        """
        for username, user in self.users.items():
            if user.current is True:
                for bucketlist_name, bucketlist in user.bucketlists.items():
                    bucketlist.rename_bucketlist_item_keys()
                    if bucketlist.current is True:
                        for bucketitem_name, bucketitem in bucketlist.bucketlist_items.items():
                            if bucketitem.current is True:
                                bucketitem.current = False
                                return True
            
    def edit_bucketlist_item(self, name, description):
        """
        Edit a bucketlist using the strings name and description.
        """
        for username, user in self.users.items():
            if user.current is True:
                for bucketlist_name, bucketlist in user.bucketlists.items():
                    bucketlist.rename_bucketlist_item_keys()
                    if bucketlist.current is True:
                        for bucketitem_name, bucketitem in bucketlist.bucketlist_items.items():
                            if bucketitem.current is True:
                                bucketitem.name = name
                                bucketitem.description = description
                                self.return_bucketlist_item()
                                return True
                        else:
                            return False
        

