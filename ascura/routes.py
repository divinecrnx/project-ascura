from flask import render_template, url_for, flash, redirect
from ascura import app

@app.route('/')
def home():
    return render_template('index.html')