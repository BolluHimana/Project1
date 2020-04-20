import os, csv
from flask import Flask, render_template, request
from model import *

APP = Flask(__name__)

APP.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
APP.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(APP)
def main():
    db.create_all()
    with open("books.csv", 'r') as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            newBook = Book(row[0], row[1], row[2], int(row[3]))
            db.session.add(newBook)
    db.session.commit()

if __name__ == "__main__":
  with APP.app_context():
      main()
