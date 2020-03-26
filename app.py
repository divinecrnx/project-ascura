from flask import Flask, render_template, flash, redirect, url_for, session, request, logging

# Init app
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.secret_key = 'secret123'
    app.run(debug=True)