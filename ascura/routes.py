import secrets, os
from PIL import Image
from flask import render_template, url_for, flash, redirect, request
from ascura import app, db, bcrypt
from ascura.forms import SCETRegistrationForm, SMARTRegistrationForm, SBMRegistrationForm, SSSRegistrationForm, SAATRegistrationForm, SHTMRegistrationForm, LoginForm, UpdateStudentAccountForm
from ascura.models import Role, School, Course, SPost, SComment, FPost, FComment, Faculty, Student
from flask_login import login_user, current_user, logout_user, login_required

@app.route("/")
@app.route("/home")
def home():
    return render_template('index.html')

@app.route("/register")
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))

    return render_template('registerl.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/register/student/scet", methods=['GET', 'POST'])
def register_scet():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = SCETRegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        
        student = Student(matrix=form.matrix.data, password=hashed_password,\
        first_name=form.first_name.data, last_name=form.last_name.data,\
        role_id=1, school_id=1, course_id=form.course.data,\
        semester=form.semester.data, email=form.email.data)

        db.session.add(student)
        db.session.commit()

        flash('Account created for {matrix} {fn} {ln}'.format(matrix=form.matrix.data, fn=form.first_name.data, ln=form.last_name.data), 'success')
        return redirect(url_for('login'))
    return render_template('register.html', form=form, title='Register SCET')

@app.route("/register/student/smart", methods=['GET', 'POST'])
def register_smart():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = SMARTRegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        
        student = Student(matrix=form.matrix.data, password=hashed_password,\
        first_name=form.first_name.data, last_name=form.last_name.data,\
        role_id=1, school_id=2, course_id=form.course.data,\
        semester=form.semester.data, email=form.email.data)

        db.session.add(student)
        db.session.commit()

        flash('Account created for {matrix} {fn} {ln}'.format(matrix=form.matrix.data, fn=form.first_name.data, ln=form.last_name.data), 'success')
        return redirect(url_for('login'))
    return render_template('register.html', form=form, title='Register SMART')

@app.route("/register/student/sbm", methods=['GET', 'POST'])
def register_sbm():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = SBMRegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        
        student = Student(matrix=form.matrix.data, password=hashed_password,\
        first_name=form.first_name.data, last_name=form.last_name.data,\
        role_id=1, school_id=3, course_id=form.course.data,\
        semester=form.semester.data, email=form.email.data)

        db.session.add(student)
        db.session.commit()

        flash('Account created for {matrix} {fn} {ln}'.format(matrix=form.matrix.data, fn=form.first_name.data, ln=form.last_name.data), 'success')
        return redirect(url_for('login'))
    return render_template('register.html', form=form, title='Register SBM')

@app.route("/register/student/sss", methods=['GET', 'POST'])
def register_sss():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = SSSRegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        
        student = Student(matrix=form.matrix.data, password=hashed_password,\
        first_name=form.first_name.data, last_name=form.last_name.data,\
        role_id=1, school_id=6, course_id=form.course.data,\
        semester=form.semester.data, email=form.email.data)

        db.session.add(student)
        db.session.commit()

        flash('Account created for {matrix} {fn} {ln}'.format(matrix=form.matrix.data, fn=form.first_name.data, ln=form.last_name.data), 'success')
        return redirect(url_for('login'))
    return render_template('register.html', form=form, title='Register SSS')

@app.route("/register/student/shtm", methods=['GET', 'POST'])
def register_shtm():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = SHTMRegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        
        student = Student(matrix=form.matrix.data, password=hashed_password,\
        first_name=form.first_name.data, last_name=form.last_name.data,\
        role_id=1, school_id=4, course_id=form.course.data,\
        semester=form.semester.data, email=form.email.data)

        db.session.add(student)
        db.session.commit()

        flash('Account created for {matrix} {fn} {ln}'.format(matrix=form.matrix.data, fn=form.first_name.data, ln=form.last_name.data), 'success')
        return redirect(url_for('login'))
    return render_template('register.html', form=form, title='Register SHTM')

@app.route("/register/student/saat", methods=['GET', 'POST'])
def register_saat():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = SAATRegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        
        student = Student(matrix=form.matrix.data, password=hashed_password,\
        first_name=form.first_name.data, last_name=form.last_name.data,\
        role_id=1, school_id=5, course_id=form.course.data,\
        semester=form.semester.data, email=form.email.data)

        db.session.add(student)
        db.session.commit()

        flash('Account created for {matrix} {fn} {ln}'.format(matrix=form.matrix.data, fn=form.first_name.data, ln=form.last_name.data), 'success')
        return redirect(url_for('login'))
    return render_template('register.html', form=form, title='Register SAAT')

@app.route("/login", methods=['GET', 'POST'])
def login():
    # print(current_user.is_authenticated)
    if current_user.is_authenticated:
        # print('Authenticated user found')
        return redirect(url_for('home'))
    # else:
    #     print('No user authenticated.')
    form = LoginForm()
    if form.validate_on_submit():
        user_student = Student.query.filter_by(email=form.email.data).first()
        user_faculty = Faculty.query.filter_by(email=form.email.data).first()
        
        if user_student and bcrypt.check_password_hash(user_student.password, form.password.data):
            # print('Logged in student')
            login_user(user_student, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        elif user_faculty and bcrypt.check_password_hash(user_faculty.password, form.password.data):
            # print('Logged in faculty')
            login_user(user_faculty, remember=form.remember.data)
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