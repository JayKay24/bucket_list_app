"""
This module defines the routes to be used by the flask application instance.
"""
from flask import render_template
from app import app

@app.route('/')
def homepage():
    """
    Return and render homepage.html template.
    """
    return render_template('homepage.html')