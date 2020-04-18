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