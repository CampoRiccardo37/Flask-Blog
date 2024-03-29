from datetime import datetime
from blog import db 

from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=datetime.now)
    username = db.Column(db.String(12),unique=True,nullable=False)
    email = db.Column(db.String(50),unique=True,nullable=False)
    password = db.Column(db.String(250),nullable=False)
    posts = db.relationship('Post',backref='author',lazy='dynamic')

    def __repr__(self):
        return f"User('{ self.id }', '{ self.username }', '{ self.email }')"

    def set_password_hash(self,password): #link di flask/python
        self.password = generate_password_hash(password)
        pass
    
    def check_password(self,password):
        return check_password_hash(self.password,password)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'),nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now)
    title = db.Column(db.String(50),nullable=False)
    description = db.Column(db.String(250),nullable=False)
    body = db.Column(db.Text(),nullable=False)
    
    def __repr__(self):
        return f"Post('{ self.id }', '{ self.title }')"

from blog import models, routes