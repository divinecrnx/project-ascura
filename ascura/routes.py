from flask import render_template, url_for, flash, redirect
from ascura import app
from ascura.forms import RegistrationForm, LoginForm
from ascura.models import Role, School, Course, SPost, SComment, FPost, FComment, Faculty, Student

@app.route("/")
@app.route("/home")
def home():
    return render_template('index.html')

@app.route("/register")
def register():
    form = RegistrationForm()
    return render_template('register.html', form=form, title='Register')

@app.route("/register_test")
def register_test():
    form = RegistrationForm()
    return render_template('register_test.html', form=form, title='Register')

@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html', form=form)