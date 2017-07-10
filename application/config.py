"""
This module contains the a class Configuration used to store the flask application
instance configuration.
"""
import os

class Configuration(object): # Instruct Flask to run the application in DEBUG mode.
    """
    Class containing configuration for the flask application instance.
    """
    DEBUG = True,
    # A cryptographic random generator to set the SECRET key.
    SECRET_KEY = os.urandom(24)
    