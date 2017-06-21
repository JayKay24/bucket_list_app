"""
This module defines the routes to be used by the flask application instance.
"""
from flask import render_template, redirect, request, url_for, flash
from forms import RegistrationForm, LoginForm
from app import app
from models.user import User
from data_store import users

@app.route('/')
def homepage():
    """
    Return and render homepage.html template.
    """
    return render_template('homepage.html')
    
@app.route('/register', methods=['GET', 'POST'])
def register():
    """
    Return and render register.html template.
    """
    if request.method == 'POST':
        form = RegistrationForm(request.form)
        if form.validate():
            first_name = str(form.first_name.data)
            last_name = form.last_name.data
            email = form.email.data
            password = form.email.data
            user = User(first_name, last_name, email, password)
            print(user.fname, user.lname)
            users.append(user)
            flash('User created successfully!', 'success')
            return redirect(url_for('login'))
    else:
        form = RegistrationForm()
    return render_template('register.html', form=form)
        
@app.route('/login', methods=['GET', 'POST'])
def login():
    """
    Return and render login.html template.
    """
    if request.method == 'POST':
        form = LoginForm(request.form)
        if form.validate():
            email = form.email.data
            password = form.password.data
            for user in users:
                if user.email == email and user.password == password:
                    flash('You have been successfully logged in!', 'success')
                    return redirect(url_for('homepage'))
                    break
            else:
                flash('Please register with the application first', 'success')
                return redirect(url_for('register'))
    else:
        form = RegistrationForm()
    return render_template('login.html', form=form)