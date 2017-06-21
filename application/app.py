"""
This module contains the file application instance.
"""

from flask import Flask, g
from flask.ext.login import LoginManager, current_user

from config import Configuration # Import the configuration data.

# Create a flask application instance.
app = Flask(__name__)
app.config.from_object(Configuration)

login_manager = LoginManager(app)
login_manager.login_view = "login"

# Create a signal handler to load the current user.
@app.before_request
def _before_request():
    g.user = current_user