"""
This module defines a BucketList class to create a BucketList object.
"""
class BucketList:
    def __init__(self, name=None, description=None, user=None):
        self.bucket_list_id = None
        self.name = name
        self.description = description
        self.user_id = user
        self.bucket_list_items = []
        
    def get_bucket_list_items(self):
        return self.bucket_list_items