"""
This module defines a class to create a User object.
"""
class User:
    def __init__(self, first_name, last_name):
        self.user_id = None
        self.fname = first_name
        self.lname = last_name
        self.email = None
        self.password = None
        # Store the user's bucketlists in a list.
        self.bucket_lists = []
        
    def get_full_name(self):
        """
        Return the user's full name.
        """
        return self.fname + self.lname
        