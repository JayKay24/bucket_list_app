"""
This module defines the routes to be used by the flask application instance.
"""
from flask import render_template, redirect, request, url_for, flash, session

from forms import RegistrationForm, LoginForm, BucketListForm
from models.user import User
from models.bucket_list import BucketList
from data_store import all_bucketlists
from app import app

user = None

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
            first_name = form.first_name.data
            last_name = form.last_name.data
            email = form.email.data
            password = form.email.data
            user = User(first_name, last_name, email, password)
            if user.email in app.config['EMAIL'] and user.password in app.config['PASSWORD']:
                flash('User already registered!', 'success')
                return redirect(url_for('login'))
            app.config['EMAIL'].append(user.email)
            app.config['PASSWORD'].append(user.password)
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
            if email in app.config['EMAIL'] and password in app.config['PASSWORD']:
                flash('You have been successfully logged in!', 'success')
                session['logged_in'] = True
                return redirect(url_for('homepage'))
            else:
                flash('Please register with the application first', 'danger')
                return redirect(url_for('register'))
    else:
        form = RegistrationForm()
    return render_template('login.html', form=form)
    
@app.route('/logout', methods=['GET'])
def logout():
    """
    Return the user back to the homepage.
    """
    session.pop('email', None)
    session.pop('password', None)
    session.pop('logged_in', None)
    flash('You were logged out', 'success')
    return redirect(url_for('homepage'))
    
    
@app.route('/show-bucketlists')
def show_all_bucketlists():
    """
    Display all bucket lists.
    """
    return render_template('show_bucketlists.html', 
                           all_bucketlists=all_bucketlists)
                           
@app.route('/create-bucketlist', methods=['GET', 'POST'])
def create_bucket_list():
    """
    Create a bucketlist for the user.
    """
    if request.method == 'POST':
        form = BucketListForm(request.form)
        if form.validate():
            name = form.name.data
            description = form.description.data
            bucket_list = BucketList(name, description, user)
            all_bucketlists.append(bucket_list)
            flash('Bucket List has been successfully created!', 'success')
            return redirect(url_for('show_all_bucketlists'))
    else:
        form = BucketListForm()
    return render_template('create_bucketlist.html', form=form)
 

            