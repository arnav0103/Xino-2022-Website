from Tool import db,login_manager
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User(db.Model,UserMixin):

    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(64),unique=True,index=True)
    school = db.Column(db.String)
    password_hash = db.Column(db.String)
    question = db.Column(db.Integer)
    answer_time = db.Column(db.DateTime,nullable = False,default=datetime.now)
    restricted = db.Column(db.String,default = "No")
    ip = db.Column(db.String,nullable = True)

    logs = db.relationship('Logs' , backref = 'user' , lazy = 'dynamic')
    def __init__(self,username,password,question,school):
        self.username = username
        self.password_hash = generate_password_hash(password)
        self.question = question
        self.school = school

    def check_password(self,password):
        return check_password_hash(self.password_hash,password)

class Logs(db.Model):
    __tablename__ = 'logs'
    id = db.Column(db.Integer , primary_key = True)
    answer_time = db.Column(db.DateTime,nullable = False)
    answer = db.Column(db.String)
    question = db.Column(db.Integer)
    userid = db.Column(db.Integer , db.ForeignKey('users.id'))

    def __init__(self,answer,answer_time,question,userid):
        self.answer = answer
        self.question = question
        self.answer_time = answer_time
        self.userid = userid


class Questions(db.Model):
    __tablename__ = 'questions'
    id = db.Column(db.Integer , primary_key = True)
    question = db.Column(db.String)
    answer = db.Column(db.String)
    source = db.Column(db.String)
    imgur = db.Column(db.String,default = "uv_nalla")

    def __init__(self,answer,question,source):
        self.answer = answer
        self.question = question
        self.source = source
