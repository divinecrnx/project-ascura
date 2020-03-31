from flask import render_template, url_for, flash, redirect
from ascura import app
from ascura.models import Role, School, Course, SPost, SComment, FPost, FComment, Faculty, Student

@app.route('/')
def home():
    return render_template('index.html')