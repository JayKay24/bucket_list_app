"""
This module defines the routes to be used by the flask application instance.
"""
from flask import render_template
from forms import RegistrationForm
from app import app

@app.route('/')
def homepage():
    """
    Return and render homepage.html template.
    """
    return render_template('homepage.html')
    
@app.route('/register')
def register():
    """
    Return and render register.html template.
    """
    return render_template('register.html')