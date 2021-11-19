

from . import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    email = db.Column(db.String, unique = True,index=True)
    password = db.Column(db.String(255))
    post_id = db.Column(db.Integer,db.ForeignKey('posts.id'))


    @property
    def password():
        raise AttributeError('you cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.password = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password,password)

    def __repr__(self):
        return f'user{self.username}'


class Post(db.Model):
    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(255))
    content = db.Column(db.String(255))
    submited = db.Column(db.DateTime, default=datetime.utcnow)
    users = db.relationship('User',backref = 'post',lazy="dynamic")

    def __repr__(self) :
        return f'post{self.content}'


    


    