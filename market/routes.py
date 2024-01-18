from market import app
from flask import render_template,redirect,url_for,flash,get_flashed_messages
from market.models import User
from market.models import Item
from market.forms import RegisterForm
from market import db

#flash is an inbuilt way of flask to ping the errors that gets rendered from validations

#when sending data from client to server you need to be carefull about crossite forgery its a way of stealing or accessing database

@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')



@app.route('/market')
def market_page():
    items = Item.query.all()
    return render_template('market.html', items=items)

#creating a new object of the Registerform class and passing it to register.html
@app.route('/register',methods=['GET','POST'])
def register_page():
    form =RegisterForm() 
    if form.validate_on_submit():
        user_to_create=User(username=form.username.data,
        email_address=form.email_address.data,
        password_hash = form.password1.data)
        #adding the user to db
        db.session.add(user_to_create)
        db.session.commit()
        #its not a good practice to give urls as hard coded values that why the method is called below
        return redirect(url_for('market_page')) 
    #This is a built in dictionary so need to check if its empty or not
    if form.errors !={}: #if there are no errors from validation
        for err_msg in form.errors.values():
            #we can give the messages a category 
            flash(f'There was an error with creating a user:{err_msg}',category='danger')
    return render_template('register.html',form=form)
