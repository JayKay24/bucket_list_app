"""
This module defines a BucketList class to create a BucketList object.
"""
class BucketList:
    def __init__(self, name=None, description=None, user=None):
        self.name = name
        self.description = description
        self.user= user
        self.current = False
        self.bucketlist_items = {}
        
    def get_full_name(self):
        """
        Concatenate the name and description of this object.
        """
        return self.name + self.description