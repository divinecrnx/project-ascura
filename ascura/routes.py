from flask import render_template, url_for, flash, redirect
from ascura import app, db, bcrypt
from ascura.forms import SCETRegistrationForm, SMARTRegistrationForm, SBMRegistrationForm, SSSRegistrationForm, SAATRegistrationForm, SHTMRegistrationForm, LoginForm
from ascura.models import Role, School, Course, SPost, SComment, FPost, FComment, Faculty, Student

@app.route("/")
@app.route("/home")
def home():
    return render_template('index.html')

@app.route("/register")
def register():
    return "<h1>Add a register landing page here.</h1>"

@app.route("/register/student/scet", methods=['GET', 'POST'])
def register_scet():
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
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', form=form)