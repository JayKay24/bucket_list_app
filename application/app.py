"""
This module contains the file application instance.
"""

from flask import Flask

from config import Configuration # Import the configuration data.

# Create a flask application instance.
app = Flask(__name__)
app.config.from_object(Configuration)