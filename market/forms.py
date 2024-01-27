# when rendering a form that will be submitted by users, a secret key is often used for security purposes. 
# This key is known as the "CSRF token" or "secret key," CSRF attacks involve a malicious website or script tricking 
# a user's browser into making an unintended request to a different site where the user is authenticated. This could 
# lead to actions being performed without the user's consent or knowledge,
#this is somewhat like models we will be using classes and we will be creating fields inside those
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import Length,EqualTo,Email,DataRequired,ValidationError
from market.models import User


#speciality in validators libarary - by writing functions using the prefix validate keyword and _ it will allow FlaskForm to execute automatically if next name is somwhere in the fields list
class RegisterForm(FlaskForm):

    def validate_username(self,username_to_check):
        user=User.query.filter_by(username=username_to_check.data).first()
        user2=User.query.filter_by(username=username_to_check.data)
        if user:
            raise ValidationError('Username already exists! Please try a different username')

    def validate_email_address(self,email_address_to_check):
        email_address=User.query.filter_by(email_address=email_address_to_check.data).first()
        if email_address:
            raise ValidationError('Email Address already exists! Please try a different email address')

    username=StringField(label='User Name',validators=[Length(min=2,max=30),DataRequired()])
    email_address=StringField(label='Email',validators=[Email(),DataRequired()])
    password1=PasswordField(label='Password',validators=[Length(min=8),DataRequired()])
    password2=PasswordField(label='Confirm Password',validators=[EqualTo('password1'),DataRequired()])
    submit=SubmitField(label='Create Account')

class LoginForm(FlaskForm):
    username = StringField(label='User Name:',validators=[DataRequired()])
    password = PasswordField(label='Password:',validators=[DataRequired()])
    submit=SubmitField(label='Login')