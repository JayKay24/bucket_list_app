"""
This module defines the routes to be used by the flask application instance.
"""
from flask import render_template, redirect, request, url_for, flash, session

from bucket_list_app import BucketListApp, all_users, all_bucketlists
from forms import RegistrationForm, LoginForm, BucketListForm
from models.bucket_list import BucketList

current_user = None
from app import app

bucket_list_app = BucketListApp()

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
            password = form.password.data
            
            response = bucket_list_app.create_user(first_name, last_name, 
                                                   email, password)
            if response is True:
                flash('User created successfully!', 'success')
                return redirect(url_for('login'))
            else:
                flash('User already registered!', 'danger')
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
            
            response = bucket_list_app.load_user(email, password)
            print(response)
            if response is True:
                flash('You have been successfully logged in!', 'success')
                session['logged_in'] = True
                return redirect(url_for('homepage'))
            else:
                flash('Please register with the application first', 'danger')
                return redirect(url_for('register'))
                
    else:
        form = LoginForm()
    return render_template('login.html', form=form)
    
@app.route('/logout', methods=['GET'])
def logout():
    """
    Return the user back to the homepage.
    """
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
            
            response = bucket_list_app.create_bucketlist(name, description)
            if response is True:
                flash('Bucketlist has been successfully created!', 'success')
            elif response is False:
                flash('Bucketlist already exists!', 'danger')
            return redirect(url_for('show_all_bucketlists'))
    else:
        form = BucketListForm()
    return render_template('create_bucketlist.html', form=form)
 
@app.route('/delete-bucketlist/<name>/<description>')
def delete_bucketlist(name, description):
    """
    Delete a bucketlist in the application.
    """
    for i in range(len(all_bucketlists)):
        if (all_bucketlists[i].name == name and
        all_bucketlists[i].description == description):
            del all_bucketlists[i]
            flash('Bucketlist successfully deleted!', 'success')
            return redirect(url_for('show_all_bucketlists', 
                                    all_bucketlists=all_bucketlists))
                                    
@app.route('/edit-bucketlist/<name>/<description>', methods=['GET', 'POST'])
def edit_bucket_list(name, description):
    """
    Edit a bucketlist in the application.
    """
    bucketlist = None
    for i in range(len(all_bucketlists)):
        if (all_bucketlists[i].name == name and 
        all_bucketlists[i].description == description):
            bucketlist = all_bucketlists.pop(i)
    if request.method == 'POST':
        form = BucketListForm(request.form, obj=bucketlist)
        if form.validate():
            name = form.name.data
            description = form.name.description
            bucketlist = BucketList(name, description)
            all_bucketlists.append(bucketlist)
            flash('Bucketlist has been successfully edited!', 'success')
            return redirect(url_for('show_all_bucketlists'))
    else:
        form = BucketListForm(obj=bucketlist)
    return render_template('edit_bucketlist.html', form=form, bucketlist=bucketlist)
    