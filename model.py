from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class model(db.Model):
    __tablename__ = "model"
    username = db.Column(db.String,primary_key=True)
    mailID = db.Column(db.String,primary_key=True)
    phone = db.Column(db.String,primary_key = True)
    pwd = db.Column(db.String,nullable=False)
    creationtimestamp=db.Column(db.DateTime(timezone=True),nullable=False)

    def __init__(self,username,mailID,phone,pwd):
        self.username=username
        self.mailID=mailID
        self.phone=phone
        self.pwd=pwd
        self.creationtimestamp=datetime.now()
class Book(db.Model):
    __tablename__ = "books"
    id = db.Column(db.Integer, primary_key=True)
    isbn = db.Column(db.String(80), index=False, unique=True, nullable=False)
    title = db.Column(db.String(80), index=True, unique=False, nullable=False)
    author = db.Column(db.String(128))
    year = db.Column(db.Integer, index=False, unique=False, nullable=False)

    def __init__(self, isbn, title, author, year) :
        self.isbn = isbn
        self.title = title
        self.author = author
        self.year = year

    def __repr__(self):
        return self.title