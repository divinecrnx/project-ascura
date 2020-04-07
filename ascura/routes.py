import secrets, os
from PIL import Image
from flask import render_template, url_for, flash, redirect, request, abort
from ascura import app, db, bcrypt
from ascura.forms import FacultyRegistrationForm, SCETRegistrationForm, SMARTRegistrationForm, SBMRegistrationForm, SHTMRegistrationForm, SAATRegistrationForm, SSSRegistrationForm, LoginForm, UpdateStudentAccountForm, PostForm
from ascura.models import Role, School, Course, UserType, User, Post, Comment
from flask_login import login_user, current_user, logout_user, login_required
from sqlalchemy import or_, and_

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

@app.route("/register/faculty/<string:school>", methods=['GET', 'POST'])
@login_required
def register_faculty(school):
    form = FacultyRegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')

        user = None # Init var
        
        if school == 'scet':
            user = User(first_name=form.first_name.data, last_name=form.last_name.data,\
            username=form.username.data, email=form.email.data, password=hashed_password,\
            school_id=1, role_id=form.role.data)
        elif school == 'smart':
            user = User(first_name=form.first_name.data, last_name=form.last_name.data,\
            username=form.username.data, email=form.email.data, password=hashed_password,\
            school_id=2, role_id=form.role.data)
        elif school == 'sbm':
            user = User(first_name=form.first_name.data, last_name=form.last_name.data,\
            username=form.username.data, email=form.email.data, password=hashed_password,\
            school_id=3, role_id=form.role.data)
        elif school == 'shtm':
            user = User(first_name=form.first_name.data, last_name=form.last_name.data,\
            username=form.username.data, email=form.email.data, password=hashed_password,\
            school_id=4, role_id=form.role.data)
        elif school == 'saat':
            user = User(first_name=form.first_name.data, last_name=form.last_name.data,\
            username=form.username.data, email=form.email.data, password=hashed_password,\
            school_id=5, role_id=form.role.data)
        elif school == 'sss':
            user = User(first_name=form.first_name.data, last_name=form.last_name.data,\
            username=form.username.data, email=form.email.data, password=hashed_password,\
            school_id=6, role_id=form.role.data)

        db.session.add(user)
        db.session.commit()

        flash('Account created for {username}'.format(username=form.username.data), 'success')
        return redirect(url_for('login'))
    
    if current_user.u_type == 1:
        return render_template('register_f.html', form=form, title='Faculty Register')
    else:
        abort(403)


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

def save_picture(form_picture): # Resizes an uploaded profile picture
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

@app.route("/<string:school>/members", methods=['GET'])
@login_required
def school_s_list(school):
    if school == 'scet':
        members = User.query.filter_by(school_id=1).all()
        return render_template('members_list.html', members=members)
    elif school == 'smart':
        members = User.query.filter_by(school_id=2).all()
        return render_template('members_list.html', members=members)
    elif school == 'sbm':
        members = User.query.filter_by(school_id=3).all()
        return render_template('members_list.html', members=members)
    elif school == 'shtm':
        members = User.query.filter_by(school_id=4).all()
        return render_template('members_list.html', members=members)
    elif school == 'saat':
        members = User.query.filter_by(school_id=5).all()
        return render_template('members_list.html', members=members)
    elif school == 'sss':
        members = User.query.filter_by(school_id=6).all()
        return render_template('members_list.html', members=members)
    else:
        return '<h1>FALSE</h1>' # Change this to something else later

@app.route("/<string:school>", methods=['GET'])
@login_required
def school_page(school):

    school_img = url_for('static', filename='images/' + school + 'logo.png')
    students_list_link = url_for('school_s_list', school=school)
    new_post_link = url_for('new_post', school=school)

    if school == 'scet':
        students = User.query.filter(User.school_id==1, or_(User.role_id==1, User.role_id==2, User.role_id==3)).all()
        lecturers = User.query.filter(User.school_id==1, or_(User.role_id==4, User.role_id==5, User.role_id==6)).all()
        posts = Post.query.filter(Post.school_id==1).all()
        comments = Comment.query.filter(Comment.school_id==1).all()
    elif school == 'smart':
        students = User.query.filter(User.school_id==2, or_(User.role_id==1, User.role_id==2, User.role_id==3)).all()
        lecturers = User.query.filter(User.school_id==2, or_(User.role_id==4, User.role_id==5, User.role_id==6)).all()
        posts = Post.query.filter(Post.school_id==2).all()
        comments = Comment.query.filter(Comment.school_id==2).all()
    elif school == 'sbm':
        students = User.query.filter(User.school_id==3, or_(User.role_id==1, User.role_id==2, User.role_id==3)).all()
        lecturers = User.query.filter(User.school_id==3, or_(User.role_id==4, User.role_id==5, User.role_id==6)).all()
        posts = Post.query.filter(Post.school_id==3).all()
        comments = Comment.query.filter(Comment.school_id==3).all()
    elif school == 'shtm':
        students = User.query.filter(User.school_id==4, or_(User.role_id==1, User.role_id==2, User.role_id==3)).all()
        lecturers = User.query.filter(User.school_id==4, or_(User.role_id==4, User.role_id==5, User.role_id==6)).all()
        posts = Post.query.filter(Post.school_id==4).all()
        comments = Comment.query.filter(Comment.school_id==4).all()
    elif school == 'saat':
        students = User.query.filter(User.school_id==5, or_(User.role_id==1, User.role_id==2, User.role_id==3)).all()
        lecturers = User.query.filter(User.school_id==5, or_(User.role_id==4, User.role_id==5, User.role_id==6)).all()
        posts = Post.query.filter(Post.school_id==5).all()
        comments = Comment.query.filter(Comment.school_id==5).all()
    elif school == 'sss':
        students = User.query.filter(User.school_id==6, or_(User.role_id==1, User.role_id==2, User.role_id==3)).all()
        lecturers = User.query.filter(User.school_id==6, or_(User.role_id==4, User.role_id==5, User.role_id==6)).all()
        posts = Post.query.filter(Post.school_id==6).all()
        comments = Comment.query.filter(Comment.school_id==6).all()
    else:
        return '<h1>FALSE</h1>' # Change this to something else later
    
    return render_template('school.html', title=school.upper(),\
        student_num=len(students),\
        lecturer_num=len(lecturers),\
        school_img=school_img,\
        students_list_link=students_list_link, new_post_link=new_post_link,\
        posts=posts, comments=comments)

@app.route("/<string:school>/post/new", methods=['GET', 'POST'])
@login_required
def new_post(school):

    if current_user.school.school_name.lower() != school:
        return redirect(url_for('school_page', school=school))
    
    school_img = url_for('static', filename='images/' + school + 'logo.png')

    form = PostForm()
    if form.validate_on_submit():
        if school == 'scet':
            s_id = 1
        elif school == 'smart':
            s_id = 2
        elif school == 'sbm':
            s_id = 3
        elif school == 'shtm':
            s_id = 4
        elif school == 'saat':
            s_id = 5
        elif school == 'sss':
            s_id = 6
        else:
            return '<h1>FALSE</h1>' # Change this to something else later
        post = Post(title=form.title.data, content=form.content.data, author=current_user, school_id=s_id)
        db.session.add(post)
        db.session.commit()
        flash('Your post has been created!', 'success')
        return redirect(url_for('school_page', school=school))
    return render_template('create_post.html', title=school.upper(),
                           form=form, legend=school.upper() + '- New Post', school_img=school_img)

@app.route("/<string:school>/post/<int:post_id>")
def post(school, post_id):
    school_img = url_for('static', filename='images/' + school + 'logo.png')

    post = Post.query.get_or_404(post_id)
    return render_template('post.html', title=post.title, post=post, school_img=school_img)

@app.route("/<string:school>/post/<int:post_id>/update", methods=['GET', 'POST'])
@login_required
def update_post(school, post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    form = PostForm()
    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data
        db.session.commit()
        flash('Your post has been updated!', 'success')
        return redirect(url_for('post', school=post.school.school_name.lower(), post_id=post.id))
    elif request.method == 'GET':
        form.title.data = post.title
        form.content.data = post.content
    return render_template('create_post.html', title='Update Post',
                           form=form, legend='Update Post')

@app.route("/<string:school>/post/<int:post_id>/delete", methods=['GET', 'POST'])
@login_required
def delete_post(school, post_id):
    post = Post.query.get_or_404(post_id)
    comments = Comment.query.filter(Comment.post_id==post_id).all()
    if post.author != current_user:
        abort(403)
    db.session.delete(post)
    for comment in comments:
        db.session.delete(comment)
    db.session.commit()
    flash('Your post has been deleted!', 'success')
    return redirect(url_for('school_page', school=school))