"""
This module contains the file application instance.
"""
from models.user import User
from models.bucket_list import BucketList
from models.bucket_list_item import BucketListItem

from flask import Flask, g

from config import Configuration # Import the configuration data.

# Create a flask application instance.
app = Flask(__name__)
app.config.from_object(Configuration)
# Enable flask to import multiple configurations and use the setting
# defined in the last import.
app.config.from_envvar('BUCKETLIST_SETTINGS', silent=True)

