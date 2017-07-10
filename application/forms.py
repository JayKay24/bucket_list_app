"""
This module defines classes used to implement wtforms.
"""
import wtforms

from wtforms import validators

class RegistrationForm(wtforms.Form):
    """
    Class used to create the fields used in the registration page.
    """
    first_name = wtforms.StringField("First name", 
                                validators=[validators.DataRequired()])
                                
    last_name = wtforms.StringField("Last name", 
                                validators=[validators.DataRequired()])
                                
    email = wtforms.StringField("Email", 
                                validators=[validators.Email()])
                                
    password = wtforms.PasswordField("Password",
                                validators=[validators.DataRequired()])
                                
    reenter_password = wtforms.PasswordField("Re-enter Password",
                                validators=[validators.DataRequired()])
                                
                                
class LoginForm(wtforms.Form):
    """
    Class used to create the fields used in the login page.
    """
    email = wtforms.StringField("Email", 
                                validators=[validators.Email()])
                                
    password = wtforms.PasswordField("Password",
                                validators=[validators.DataRequired()])
                                
class BucketListForm(wtforms.Form):
    """
    Class used to create the fields used in the show_bucketlist page.
    """
    name = wtforms.StringField('Name', 
                               validators=[validators.DataRequired()])
                               
    description = wtforms.TextAreaField('Description', 
                                validators=[validators.DataRequired()])
                                
                                
                                