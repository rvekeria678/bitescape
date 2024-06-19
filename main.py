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
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
#----Create Database----#
class Base(DeclarativeBase): pass
#----Configure Tables----#
#----Configure BlogPost Table----#
class BlogPost(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    subtitle: Mapped[str] = mapped_column(String(250), nullable=False)
    date: Mapped[str] = mapped_column(String(250), nullable=False)
    body: Mapped[str] = mapped_column(Text, nullable=False)
    author = Mapped[str] = mapped_column(String(250), nullable=False)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)
#----Configure User Table----#
class User(UserMixin, db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String[100], nullable=False)
    email: Mapped[str] = mapped_column(String[100], nullable=False)
    password: Mapped[str] = mapped_column(String[100], nullable=False)
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
    return render_template('signin.html')
#----Sign-out Action----#
@app.route('/logout', methods=['GET','POST'])
def logout():
    return redirect(url_for('root'))
#----Comment Action----#

#----Server Driver----#
if __name__ == "__main__":
    app.run(debug=True)