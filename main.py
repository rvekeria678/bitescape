from flask import Flask, abort, render_template, redirect, url_for, flash
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
#----About Page----#
app.route('/about')
def about():
    return render_template('about.html')
#----Contact Page----#
app.route('/contact', methods=['GET', 'POST'])
def get_contact_info():
    return render_template('contact.html')
#----Log-in Page----#
@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('signin.html')
#----Sign-out Action----#

#----Comment Action----#

#----Server Driver----#
if __name__ == "__main__":
    app.run(debug=True)