import secrets, os
from PIL import Image
from flask import render_template, url_for, flash, redirect, request
from ascura import app, db, bcrypt
from ascura.forms import SCETRegistrationForm, SMARTRegistrationForm, SBMRegistrationForm, SHTMRegistrationForm, SAATRegistrationForm, SSSRegistrationForm, LoginForm, UpdateStudentAccountForm
from ascura.models import Role, School, Course, UserType, User, Post, Comment
from flask_login import login_user, current_user, logout_user, login_required

@app.route("/")
@app.route("/home")
def home():
    return render_template('index.html')

@app.route("/register")
def registerl():
    if current_user.is_authenticated:
        return redirect(url_for('home'))

    return render_template('registerl.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/register/student/<string:school>", methods=['GET', 'POST'])
def register(school):
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    if school == 'scet':
        form = SCETRegistrationForm()
    elif school == 'smart':
        form = SMARTRegistrationForm()
    elif school == 'sbm':
        form = SBMRegistrationForm()
    elif school == 'shtm':
        form = SHTMRegistrationForm()
    elif school == 'saat':
        form = SAATRegistrationForm()
    elif school == 'sss':
        form = SSSRegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')

        user = None # Init var
        
        if school == 'scet':
            user = User(first_name=form.first_name.data, last_name=form.last_name.data,\
            username=form.username.data, email=form.email.data, password=hashed_password,\
            school_id=1, course_id=form.course.data, semester=form.semester.data)
        elif school == 'smart':
            user = User(first_name=form.first_name.data, last_name=form.last_name.data,\
            username=form.username.data, email=form.email.data, password=hashed_password,\
            school_id=2, course_id=form.course.data, semester=form.semester.data)
        elif school == 'sbm':
            user = User(first_name=form.first_name.data, last_name=form.last_name.data,\
            username=form.username.data, email=form.email.data, password=hashed_password,\
            school_id=3, course_id=form.course.data, semester=form.semester.data)
        elif school == 'shtm':
            user = User(first_name=form.first_name.data, last_name=form.last_name.data,\
            username=form.username.data, email=form.email.data, password=hashed_password,\
            school_id=4, course_id=form.course.data, semester=form.semester.data)
        elif school == 'saat':
            user = User(first_name=form.first_name.data, last_name=form.last_name.data,\
            username=form.username.data, email=form.email.data, password=hashed_password,\
            school_id=5, course_id=form.course.data, semester=form.semester.data)
        elif school == 'sss':
            user = User(first_name=form.first_name.data, last_name=form.last_name.data,\
            username=form.username.data, email=form.email.data, password=hashed_password,\
            school_id=6, course_id=form.course.data, semester=form.semester.data)

        db.session.add(user)
        db.session.commit()

        flash('Account created for {username}'.format(username=form.username.data), 'success')
        return redirect(url_for('login'))
    return render_template('register.html', form=form, title='Register', school=school)

@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', form=form, title='Log In')

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))

def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static/images/profile_pics', picture_fn)

    output_size = (150, 150)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)

    return picture_fn

@app.route("/account", methods=['GET', 'POST'])
@login_required
def account():
    form = UpdateStudentAccountForm()
    if form.validate_on_submit():
        if form.picture.data:
            picture_file = save_picture(form.picture.data)
            current_user.image_file = picture_file
        current_user.email = form.email.data
        current_user.semester = form.semester.data
        db.session.commit()
        flash('Your account has been updated!', 'success')
        return redirect(url_for('account'))
    elif request.method == 'GET':
        form.email.data = current_user.email
        form.semester.data = current_user.semester
    image_file = url_for('static', filename='images/profile_pics/' + current_user.image_file)
    return render_template('account.html', title='Account', image_file=image_file, form=form)