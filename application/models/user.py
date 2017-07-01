"""
This module defines a class to create a User object.
"""
class User:
    def __init__(self, first_name=None, last_name=None, email=None, 
                 password=None):
        self.fname = first_name
        self.lname = last_name
        self.email = email
        self.password = password
        # Store the user's bucketlists in a dictionary.
        self.bucketlists = {}
        self.current = False
        
    def get_credentials(self):
        """
        Return the user's full name.
        """
        return self.email + self.password
