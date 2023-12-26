# when rendering a form that will be submitted by users, a secret key is often used for security purposes. 
# This key is known as the "CSRF token" or "secret key," CSRF attacks involve a malicious website or script tricking 
# a user's browser into making an unintended request to a different site where the user is authenticated. This could 
# lead to actions being performed without the user's consent or knowledge,
#this is somewhat like models we will be using classes and we will be creating fields inside those
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField

class RegisterForm(FlaskForm):
    username=StringField(label='User Name')
    email_address=StringField(label='Email')
    password1=PasswordField(label='Password')
    password2=PasswordField(label='Confirm Password')
    submit=SubmitField(label='submit')