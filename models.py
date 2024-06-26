from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    usertype = db.Column(db.String(50), nullable=False)
    token = db.Column(db.String(255), unique=True)

class FavouriteShow(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    useremail = db.Column(db.String(120), db.ForeignKey('user.email'), nullable=False)
    showid = db.Column(db.Integer, nullable=False)
    addeddate = db.Column(db.DateTime, nullable=False)
    status = db.Column(db.String(50), nullable=False)

class WatchList(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    useremail = db.Column(db.String(120), db.ForeignKey('user.email'), nullable=False)
    showid = db.Column(db.Integer, nullable=False)
    addeddate = db.Column(db.DateTime, nullable=False)
    status = db.Column(db.String(50), nullable=False)

class UserDetails(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    bio = db.Column(db.Text, nullable=True)
