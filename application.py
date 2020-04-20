import os


from flask import Flask, session,request,render_template,redirect
from flask_session import Session
from sqlalchemy import create_engine,desc
from sqlalchemy.orm import scoped_session, sessionmaker
import logging
logging.basicConfig(level=logging.DEBUG)

from model import *

app = Flask(__name__)
# Check for environment variable
if not os.getenv("DATABASE_URL"):
   raise RuntimeError("DATABASE_URL is not set")

app.config['SQLALCHEMY_DATABASE_URI'] =os.getenv("DATABASE_URL")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Configure session to use filesystem      
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)
db.init_app(app)

# Set up database
engine = create_engine(os.getenv("DATABASE_URL"))
#Session = scoped_session(sessionmaker(bind=engine))
#session=Session()
@app.route("/")
def index():
    return render_template("index.html")
@app.route("/Register", methods = ['POST', 'GET'])
def cont():
    db.create_all()
    if request.method =='POST':
        udata=model(request.form['username'],request.form['mailID'],request.form['phone'],request.form['pwd'])
        userd=model.query.filter_by(mailID=request.form['mailID']).first()
        if userd is not None:
            var='Email already exists..please login!!'
            return render_template("index.html",var=var)
        db.session.add(udata)
        db.session.commit()
        print("Sucesssfully Registered")
        var1='Registration Successful'
        return render_template("index.html",var1=var1)
    else:
        return render_template("index.html")
@app.route('/admins')
def admin():
    usersinfo = model.query.all()
    return render_template("admins.html",admin = usersinfo)
@app.route('/auth', methods=['POST'])
def log():
    LogData = model.query.filter_by(mailID= request.form['mailID']).first()
    if LogData is not None:
        if request.form['pwd'] == LogData.pwd:
            session['mailID'] = request.form['mailID']
            return redirect('/home')
        else:
            var1 = "wrong Credentials"
            return render_template('index.html', var= var1)
    else:
        var1 = "Error: You are not a registered. Please first register to login"
        return render_template("index.html",var = var1)

@app.route('/home')
def home():
    try:
        LogData = session['mailID']
        return render_template("login.html")
    except:
        var1 = "You must log in to view the homePage"
        return render_template("index.html",var=var1)

@app.route('/logout')
def logout():
    try:
        user_data = session['mailID']
        session.clear()
        var1= "Logged-Out"
        return render_template("index.html",var=var1)
    except:
        var1 = "You must first log in to logout"
        return render_template("index.html",var=var1)