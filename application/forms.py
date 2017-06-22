"""
This module defines classes used to implement wtforms.
"""
import wtforms

from wtforms import validators

class RegistrationForm(wtforms.Form):
    first_name = wtforms.StringField("First name", 
                                validators=[validators.DataRequired()])
                                
    last_name = wtforms.StringField("Last name", 
                                validators=[validators.DataRequired()])
                                
    email = wtforms.StringField("Email", 
                                validators=[validators.Email()])
                                
    password = wtforms.PasswordField("Password",
                                validators=[validators.DataRequired()])
                                
class LoginForm(wtforms.Form):
    email = wtforms.StringField("Email", 
                                validators=[validators.Email()])
                                
    password = wtforms.PasswordField("Password",
                                validators=[validators.DataRequired()])
                                
                                