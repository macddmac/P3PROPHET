from flask import Flask, flash, jsonify, redirect, url_for, render_template, Response, request, session, current_app, g
from flask_sqlalchemy import SQLAlchemy
from flask import render_template, request, Flask
from mathcalc import Math
from flask import Flask, redirect, url_for, render_template, request
from sqlalchemy.sql import text
from flask_wtf import FlaskForm
from rohanbs import RohanBubbleSort1
from wtforms import StringField, PasswordField, BooleanField, SubmitField , IntegerField
from wtforms.validators import DataRequired, Email, EqualTo
from flask_login import LoginManager, UserMixin, login_required, login_user, logout_user
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash
from werkzeug.urls import url_parse
import sqlalchemy
import requests
import os
from shekarbubblesort import Bubblesort
from sambubble import Numbersort
import requests as r
import json as j
import time
from urllib.request import Request, urlopen
#from shekarminilab import sk
app = Flask(__name__)
#app.register_blueprint(sk)
# creating a Flask instance
basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
login = LoginManager(app)
login.login_view = 'login_route'
# connects default URL of server to render home.html
dbURI = 'sqlite:///' + os.path.join(basedir, 'models/myDB.db')
""" database setup to support db examples """
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = dbURI
app.config['SECRET_KEY'] = "qwerty"
db = SQLAlchemy(app)
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(255), unique=False, nullable=False)
    last_name = db.Column(db.String(255), unique=False, nullable=False)
    username = db.Column(db.String(255), unique=True, nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
class Item(UserMixin, db.Model):
    ii = db.Column(db.Integer, primary_key=True)
    item = db.Column(db.String(255), unique=False, nullable=False)
    itemID = db.Column(db.Integer, unique=False, nullable=False)
    price = db.Column(db.Integer, unique=False, nullable=False)
    itemQuan = db.Column(db.Integer, unique=False, nullable=False)
class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    passwordconfirm = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo("password")])
    firstname = StringField('First Name', validators=[DataRequired()])
    lastname = StringField('Last Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Register')
class ItemForm(FlaskForm):
    item = StringField('Item', validators=[DataRequired()])
    itemID = IntegerField('Item ID', validators=[DataRequired()])
    price = IntegerField('Item Price', validators=[DataRequired()])
    itemQuan = IntegerField('Item Quantity', validators=[DataRequired()])
    submit = SubmitField('Enter Item')
class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')
@login.user_loader
def load_user(id):
    return User.query.get(int(id))
@app.route('/api')
def idk():
    response = requests.get('http://aws.random.cat/meow')
    image = response.json()['file']
    return render_template("api.html", image=image)
@app.route('/database')
@login_required
def index():
    data = User.query.all()
    return render_template('database.html', data=data)
# Create a sign up page
@app.route('/')
def home_route():
    #Gets the api data from web
    text = "https://cat-fact.herokuapp.com/facts/random"
    data = requests.get(text).json()["text"]
    return render_template("home.html", data=data)
    #Gets the api data from web
    #x = r.get("https://uselessfacts.jsph.pl/random.json?language=en")
    #data = j.loads(x.content) #Fetch rest api data
    #fact = data.get("text") #Fetch rest api data
    #return render_template("home.html", fact=fact) #Fetch rest api data
@app.route('/index')
def index_route():
    return render_template("index.html")

@app.route('/newanimation2')
def newanimation2_route():
    return render_template("newanimation2.html")

@app.route('/newanimation')
def newanimation_route():
    return render_template("newanimation.html")

@app.route('/animation')
def animation_route():
    return render_template("animation.html")

@app.route('/math')
@login_required
def math_route():
    return render_template("math.html")

@app.route('/math1')
def math1_route():
    return render_template("math1.html")

@app.route('/math2')
def math2_route():
    return render_template("math2.html")

@app.route('/bubblesort')
def bubblesort_route():
    return render_template("bubblesorts.html")
@app.route('/shekarminilab', methods=["GET", "POST"])
def shekarminilab_route():
    if request.form:
        all_list = []
        print("hello i am shekar")
        integer = request.form.get("string")
        arr = integer.split()
        for j in range (0,len(arr)):
            #converting all list into integers
            arr[j] = int(arr[j])
        bs = Bubblesort(integer)
        return render_template("shekarminilab.html", sorted_list=bs.sarr, input_list=arr)
    return render_template("shekarminilab.html")
@app.route('/sambubblesort', methods=["GET", "POST"])
def sambubblesort_route():
    if request.form:
        all_list = []
        print("hello i am sam")
        integer = request.form.get("string")
        arr = integer.split()
        for j in range (0,len(arr)):
            #converting all list into integers
            arr[j] = int(arr[j])
        bs = Numbersort(integer)
        return render_template("sambubblesort.html", sorted_list=bs.szeto)
    return render_template("sambubblesort.html")
@app.route('/testimonial')
def testimonial_route():
    return render_template("testmonial.html")
# connects /hello path of server to render hello.html
@app.route('/freepage')
def free_page():
    return render_template("freepage.html")
@app.route('/minilabs')
def minilabs_route():
    return render_template("minilabs.html")
@app.route('/coupon')
@login_required
def coupon():
    return render_template("coupon.html")
@app.route('/cats')
@login_required
def cats():
    text = "https://cat-fact.herokuapp.com/facts/random"
    data = requests.get(text).json()["text"]
    return render_template("cats.html", data=data)
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")
@app.route('/customerservice', methods=['POST', 'GET'])
def customer():
    if request.method == "POST":
        if request.form.get("response") == "1":
            return render_template("cats.html")
        elif request.form.get("response") == "2":
            return render_template("math.html")
        elif request.form.get("response") == "3":
            return render_template("termsconditions.html")
        elif request.form.get("response") == "4":
            return render_template("animation.html")
        else:
            return error("Please pick an option from 1-4.", 401)
    return render_template("customerservice.html")
@app.route('/secret' , methods=["GET", "POST"])
def secret_route():
    itemform = ItemForm()
    if itemform.validate_on_submit():
        newItem = Item(item=itemform.item.data, itemID=itemform.itemID.data, price=itemform.price.data, itemQuan=itemform.itemQuan.data)
        # Insert all the values into the database
        db.session.add(newItem)
        db.session.commit()
        return redirect("/secret")
    return render_template("secret.html" , form = itemform)
# connects /hello path of server to render hello.html
@app.route('/login', methods=['POST', 'GET'])
def login_route():
    logform = LoginForm()
    if logform.validate_on_submit():
        user = User.query.filter_by(username=logform.username.data).first()
        if user is None or not user.check_password(logform.password.data):
            flash("Login Failed")
            return redirect("/login")
        login_user(user)
        flash("Login Successful!")
        if logform.username.data == "secret":
            return redirect("/secret")
        nextpage = request.args.get("next")
        if not nextpage or url_parse(nextpage).netloc != '':
            return redirect('/')
        return redirect(nextpage)
    else:
        return render_template("login.html", form = logform)
@app.route("/<usr>")
def user(usr):
    return f"<h1>{usr}</h1>"
@app.route('/newuser/', methods=["GET", "POST"])
def new_user():
    regform = RegisterForm()
    """Register user"""
    if regform.validate_on_submit():
        newUser = User(username=regform.username.data, first_name=regform.firstname.data, last_name=regform.lastname.data, email=regform.email.data)
        newUser.set_password(regform.password.data)
        # Insert all the values into the database
        db.session.add(newUser)
        db.session.commit()
        return redirect("/login")
    else:
        return render_template("signup.html", form = regform)
# connects /flask path of server to render flask.html
@app.route('/signup', methods=['POST','GET'])
def signup():
    if request.method == "POST":
        newuser = request.form["newusername"] # using name as dictionary key
        # redirects us to the user page
        return redirect(url_for("newuser", newusr=newuser))
    else:
        return render_template("login.html")
@app.route("/<usr>")
def newuser(newuser):
    return f"<h1>{newuser}</h1>"
# Create a sign up page
@app.route('/rohanbubsort', methods=["GET", "POST"])
def rohanbubblesort():
    if request.form:
        all_list = []
        all_list.append(int(request.form.get('number1')))
        all_list.append(int(request.form.get('number2')))
        all_list.append(int(request.form.get('number3')))
        return render_template("rohanbubsort.html", testing=RohanBubbleSort1(all_list))
    return render_template("rohanbubsort.html")

@app.route('/hi', methods=["GET", "POST"])
def listclass():
    if request.form:
        return render_template("G.html", G=Math(int(request.form.get("series"))))
    return render_template("G.html", G=Math(1))

def bubble(inst):
    indexing_length = len(inst) - 1
    sorted = False
    while not sorted:
        sorted = True
        for i in range(0, indexing_length):
            if inst[i] > inst[i+1]:
                sorted = False
                inst[i], inst[i+1] = inst[i+1], inst[i]
    return inst

@app.route('/bubbb', methods=["GET", "POST"])
def home():
    if request.method == "POST":
        numbs = request.form['ints']
        integers = list(numbs.split())
        bubble(integers)
        return redirect(url_for("integers", ints=integers))
    return render_template("form.html")


@app.route("/<ints>")
def integers(ints):
    return f"<p>{ints}</p>"

if __name__ == "__main__":
    db.create_all()
    # runs the application on the repl development server
    app.run(debug=True)

