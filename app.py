import psycopg2
from flask import Flask, render_template, request, url_for, redirect, flash
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


# Initialize Flask class
app = Flask(__name__)

app.config['SECRET_KEY'] = '4d17463af685b8981375f095383af6ff'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:12121994@127.0.0.1:5432/flask-app'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

conn = psycopg2.connect("dbname='flask-app' user='postgres' host='localhost' password='12121994'")

# Initialize SQLAlchemy class
db = SQLAlchemy(app)

# Initialize Bcrypt
bcrypt = Bcrypt(app)

# Initialize LoginManager class
login_manager = LoginManager(app)

# from models import User 

@app.before_first_request
def create_table():
    db.create_all()
    # db.drop_all()
    
@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title = 'Home')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        firstName = request.form['firstName']
        lastName = request.form['lastName']
        email = request.form['email']
        password = request.form['password']
        user = User(firstName = firstName, lastName = lastName, email = email, password = hashed_password)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('signin'))
        flash(f'SignUp successfull', 'success')
    return render_template('signup.html', title='SignUp')


@app.route('/signin', methods=['GET', 'POST'])
def signin():
    return render_template('signin.html', title = 'SignIn')



if __name__ == '__main__':
    app.run(debug=True)