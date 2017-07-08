class BucketListItem:
    def __init__(self, name=None, description=None):
        self.name = name
        self.description = description
        self.current = False
        
    def get_full_name(self):
        """
        Concatenate the name and description of this object.
        """
        return self.name + self.description