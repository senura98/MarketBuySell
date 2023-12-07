# inherit from db.Model class
from market import db

class User(db.model):
   id = db.Column(db.Integer(), primary_key=True)
   username=db.Column(db.String(length=30),nullable=False,unique=True)
   email_address=db_Column(db.String(length=50),nullable=False,unique=True)
   password_hash=db.Column(db.String(length=60),nullable=false)
   budget=db.Column(db.Integer(),nullable=false,default=1000)


class Item(db.Model):
    #creating an instance of column class, it is a must to have the id column thats how flask identifies
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=30), nullable=False, unique=True)
    price = db.Column(db.Integer(), nullable=False)
    barcode = db.Column(db.String(length=12), nullable=False, unique=True)
    description = db.Column(db.String(length=1024), nullable=False, unique=True)

    #shows the string representation - mainly for debugging
    def __repr__(self):
        return f'Item {self.name}'
