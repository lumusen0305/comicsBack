from sqlalchemy import and_
import datetime

from extensions import db
from werkzeug.security import generate_password_hash, check_password_hash

class Account(db.Model):
    __tablename__ = 'Account'
    id = db.Column(db.String, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=True)
    password = db.Column(db.String, unique=True, nullable=True)
    email = db.Column(db.String, unique=True, nullable=True)
    def __init__(self,id, username,password,email):
        self.id=id
        self.username = username
        self.password = password
        self.email = email
    def nameaccount(self, username):
        self.username = username

    def __repr__(self):
        return '<User %r>' % self.username
    def add(self):
        self.password=generate_password_hash(self.password)
        db.session.add(self)
        db.session.commit()
    def search(self):
        admin = Account.query.filter(Account.username==self.username).first()
        return admin
    def judge_account_register(self):
        admin = Account.query.filter(Account.username==self.username).first()
        print(admin)
        if admin==None:
            return True
        else:
            return False
    def update(self,user_id):
        admin = Account.query.filter(Account.id==user_id).first()
        admin.username=self.username
        admin.password=self.password
        admin.email=self.email
        db.session.commit()
    def check(self):
        admin = Account.query.filter(Account.username==self.username).first()
        result = check_password_hash(admin.password, self.password)
        return result

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Study(db.Model):
    __tablename__ = 'Study'
    id = db.Column(db.String, primary_key=True)
    uid = db.Column(db.String, primary_key=True)
    study_hours = db.Column(db.String, unique=True, nullable=True)
    date = db.Column(db.String, unique=True, nullable=True)
    def __init__(self,id, uid,study_hours):
        self.id=id
        self.uid = uid
        self.study_hours = study_hours
    def __repr__(self):
        return '<User %r>' % self.username
    def add(self):
        x = datetime.datetime.now()  # 現在時間
        date = "{}/{}/{}".format(x.year,x.month,x.day)
        self.password=generate_password_hash(self.password)
        self.date=date
        db.session.add(self)
        db.session.commit()