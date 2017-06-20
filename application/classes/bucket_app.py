"""
This module defines a class that enables users to create, read, update and
delete bucketlists and bucketlist items.
"""
from application.classes.user import User
from application.classes.bucket_list import BucketList
from application.classes.bucket_list_item import BucketListItem

class BucketListApp:
    """
    Class used to instantiate a single BucketListApp as the main flask
    backend interface.
    """
    def __init__(self):
        self.users = {}
        self.full_name = None
        self.bucket_list = None
    
    def create_user(self, first_name, last_name):
        """
        Create a single user.
        """
        self.user = User(first_name, last_name)
        self.full_name = self.user.get_full_name()
        self.users[self.full_name] = self.user
        
    def create_bucket_list(self, name, description):
        """
        Create a bucket list.
        """
        self.bucket_list = BucketList(name, description)
        self.users[self.full_name].append(self.bucket_list)
        
    def create_bucket_list_item(self, name, description):
        """
        Create a bucket list item.
        """
        self.bucket_list_item = BucketListItem(name, description)
        self.users[self.full_name].bucket_lists.append(self.bucket_list_item)