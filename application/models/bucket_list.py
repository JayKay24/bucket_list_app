"""
This module defines a BucketList class to create a BucketList object.
"""
class BucketList:
    def __init__(self, name=None, description=None, user=None):
        self.name = name
        self.description = description
        self.user= user
        self.bucketlist_items = {}
    