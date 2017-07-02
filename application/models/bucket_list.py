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
        
    def rename_bucketlist_item_keys(self):
        """
        Reset the keys of bucketlist_items dictionary to new names.
        """
        all_values = list(self.bucketlist_items.values())
        self.bucketlist_items.clear()
        for value in all_values:
            self.bucketlist_items[value.get_full_name()] = value
