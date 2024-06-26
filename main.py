from flask import Flask, abort, render_template, redirect, request, url_for, flash, send_from_directory
from flask_bootstrap import Bootstrap5
from flask_ckeditor import CKEditor
from flask_login import UserMixin, login_user, LoginManager, current_user, logout_user
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship, DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Text
from functools import wraps
from werkzeug.security import generate_password_hash, check_password_hash
from forms import RegisterForm, LogInForm, CreateBlogForm, CreatCommentForm
from dotenv import load_dotenv
import os
#----Load Environment Vairables----#
load_dotenv()
#----Configure Flask App----#
app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
ckeditor = CKEditor(app)
Bootstrap5(app)
#----Configure Flask-Login----#

#----Create Database----#
class Base(DeclarativeBase): pass
#----Configure Tables----#
#----Configure BlogPost Table----#

#----Configure User Table----#

#----Create Tables in Database----#

#----Routing Logic----#
#----Home Page----#
@app.route('/', methods=['GET'])
def root():
    return render_template('index.html')
#----Cuisines Page----#
@app.route('/cuisines', methods=['GET', 'POST'])
def cuisines():
    return render_template('cuisines.html')
#----About Page----#
@app.route('/about', methods=['GET', 'POST'])
def about():
    return render_template('about.html')
#----Contact Page----#
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    return render_template('contact.html')
#----Log-in Page----#
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'post':
        #----Handle Log In Attempt-----#
        print("Login Attempt")
        redirect(url_for('root'))
    return render_template('signin.html')
#----Register Page----#
@app.route('/register', methods=['GET', 'POST'])
def register():
    return render_template('register.html')
#----Sign-out Action----#
@app.route('/logout', methods=['GET','POST'])
def logout():
    return redirect(url_for('root'))
#----Comment Action----#

#----Server Driver----#
if __name__ == "__main__":
    app.run(debug=True)