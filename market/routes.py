from market import app
from flask import render_template,redirect,url_for,flash,request
from market.models import User
from market.models import Item
from market.forms import RegisterForm,PurchaseItemForm,LoginForm
from flask_login import login_user,logout_user,login_required,current_user
from market import db

#sends the the form instance as an information to our template

#flash is an inbuilt way of flask to ping the errors that gets rendered from validations

#when sending data from client to server you need to be carefull about crossite forgery its a way of stealing or accessing database

@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')



@app.route('/market',methods=['GET','POST'])
@login_required
def market_page():
    purchase_form = PurchaseItemForm()
    if request.method=="POST":
        #can see the key and value pairs inside purchase form
            #print(purchase_form.__dict__)
        purchased_item=request.form.get('purchased_item')
        p_item_object=Item.query.filter_by(name=purchased_item).first()
        if p_item_object:
            #there is a field to represent ownership in the user model
            p_item_object.owner=current_user.id
            current_user.budget =  current_user.budget - p_item_object.price
            db.session.commit()
            flash(f"Congratulations! You purchased {p_item_object.name} for {p_item_object.price}")
    if request.method=="GET":
        item = Item.query.filter_by(owner=None)
        return render_template('market.html', item=item, purchase_form=purchase_form)

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
            # current_user.budget=1000
            # db.session.commit()
            flash(f'Succes! You are logged in as:{current_user.budget} {current_user.username}',category='success')
            print(current_user.budget)
            return redirect(url_for('market_page'))
        else:
            flash('Username and password are not match! Please try again',category='danger')


    return render_template('login.html',form=form)

@app.route('/logout')
def logout_page():
    logout_user()
    flash("You have been logged out!",category='info')
    return redirect(url_for("home_page"))