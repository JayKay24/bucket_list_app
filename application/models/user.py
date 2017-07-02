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
        
    def rename_bucketlist_keys(self):
        """
        Reset the keys of a bucketlists dictionary to new names.
        """
        all_values = list(self.bucketlists.values())
        self.bucketlists.clear()
        for value in all_values:
            self.bucketlists[value.get_full_name()] = value
        
