"""
This module defines a class to create a User object.
"""
class User:
    def __init__(self, first_name=None, last_name=None, email=None, 
                 password=None):
        self.user_id = None
        self.fname = first_name
        self.lname = last_name
        self.email = email
        self.password = password
        # Store the user's bucketlists in a list.
        self.bucket_lists = []
        
    def get_full_name(self):
        """
        Return the user's full name.
        """
        return self.fname + self.lname
        
    # Flask-Login interface.
    def get_id(self):
        """
        Determine ID of user to be stored in the session.
        """
        return str(self.id)
        
    # Allow users to log in only if the active attribute is set to True.
    def is_authenticated(self):
        return True
        
    def is_active(self):
        return self.active
        
    def is_anonymous(self):
        return False