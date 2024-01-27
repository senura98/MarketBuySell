#__init__ - every python package that is a regular package has this file.it turns the directory into a package. 
# this file is executed when the package is imported. This file can be used to perform any necessary initializations for the package.
#can be used for configurations as well

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
#sqlalchemy is similar to djanjo object relation mapper
#circular imports - two files trying to import from each other(onefile will miss a variable) : to avoid this 
# python executes a single file that knows how to import step by step



app = Flask(__name__)
#adding configurations - its a dictionary
#URI - uri is an identifier while url is a link
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
app.config['SECRET_KEY']='c492acd84e08f3c8002f5deb'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager =LoginManager(app)

#displays login page when login is required - this is related with login_required annotation in routes
login_manager.login_view="login_page"
login_manager.login_message_category="info"

from market import routes


