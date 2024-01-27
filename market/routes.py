from market import app
from flask import render_template,redirect,url_for,flash
from market.models import User
from market.models import Item
from market.forms import RegisterForm
from market.forms import LoginForm
from flask_login import login_user,logout_user,login_required
from market import db

#flash is an inbuilt way of flask to ping the errors that gets rendered from validations

#when sending data from client to server you need to be carefull about crossite forgery its a way of stealing or accessing database

@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')



@app.route('/market')
@login_required
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
        password = form.password1.data)
        #adding the user to db
        db.session.add(user_to_create)
        db.session.commit()
        # since a valid user is created the user can be logged in
        login_user(user_to_create)
        flash(f"Account created successfully! You are now logged in as {user_to_create.username}",category="success")
        #its not a good practice to give urls as hard coded values that why the method is called below
        return redirect(url_for('market_page')) 
    #This is a built in dictionary so need to check if its empty or not
    if form.errors !={}: #if there are no errors from validation
        for err_msg in form.errors.values():
            #we can give the messages a category 
            flash(f'There was an error with creating a user:{err_msg}',category='danger')
    return render_template('register.html',form=form)

@app.route('/login',methods=['GET','POST'])
def login_page():
    form=LoginForm()
    if form.validate_on_submit():
        attempted_user=User.query.filter_by(username=form.username.data).first()
        if attempted_user and attempted_user.check_password_correction(attempted_password=form.password.data):
            login_user(attempted_user)
            flash(f'Succes! You are logged in as: {attempted_user.username}',category='success')
            return redirect(url_for('market_page'))
        else:
            flash('Username and password are not match! Please try again',category='danger')


    return render_template('login.html',form=form)

@app.route('/logout')
def logout_page():
    logout_user()
    flash("You have been logged out!",category='info')
    return redirect(url_for("home_page"))