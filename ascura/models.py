from datetime import datetime
import pytz
from ascura import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

def get_time(): # Gets the current KL timezone time
    dt_utcnow = datetime.now(tz=pytz.UTC)
    dt_kl = dt_utcnow.astimezone(pytz.timezone('Asia/Kuala_Lumpur'))

    return dt_kl

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=get_time())
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    school_id = db.Column(db.Integer, db.ForeignKey('school.id'), nullable=False)
    comments = db.relationship('Comment', backref='post', lazy=True)

    def __repr__(self):
        return "Post('{title}', '{date_posted}')".format(title=self.title, date_posted=self.date_posted)

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_posted = db.Column(db.DateTime, nullable=False, default=get_time())
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'), nullable=False)
    school_id = db.Column(db.Integer, db.ForeignKey('school.id'), nullable=False)

    def __repr__(self):
        return "Comment('{content}', '{date_posted}')".format(content=self.content, date_posted=self.date_posted)

class Role(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    role_name = db.Column(db.String(20), nullable=False, unique=True)
    student_role = db.relationship("User", backref='role', lazy=True)

    def __repr__(self):
        return "Role('{id}', '{role_name}')".format(id=self.id, role_name=self.role_name)

class School(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    school_name = db.Column(db.String(5), nullable=False, unique=True)
    student_school = db.relationship("User", backref='school', lazy=True)

    def __repr__(self):
        return "School('{id}', '{school_name}')".format(id=self.id, school_name=self.school_name)

class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    course_name = db.Column(db.String(7), nullable=False, unique=True)
    student_course = db.relationship("User", backref='course', lazy=True)

    def __repr__(self):
        return "Course('{id}', '{course_name}')".format(id=self.id, course_name=self.course_name)

# Admin, Elevated, Normal: 1, 2, 3
class UserType(db.Model):
    __tablename__ = 'usertype'
    id = db.Column(db.Integer, primary_key=True)
    uname = db.Column(db.String(7), unique=True, nullable=False)
    user = db.relationship('User', backref='type', lazy=True)

    def __repr__(self):
        return "User Type('{utype}, {uname}')".format(utype=self.id, uname=self.uname)

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    username = db.Column(db.String(14), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    short_desc = db.Column(db.String(70), nullable=False, default="Hi there, I'm new to Ascura.")
    long_desc = db.Column(db.Text, nullable=False, default="No information given")
    interests = db.Column(db.String(100), nullable=False, default="This user has not specified any interests.")

    school_id = db.Column(db.Integer, db.ForeignKey('school.id'), nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'), nullable=True) # Faculty members don't need this
    semester = db.Column(db.String(2), nullable=True) # Faculty members don't need this

    role_id = db.Column(db.Integer, db.ForeignKey('role.id'), nullable=False, default=1) # Default student role
    u_type = db.Column(db.Integer, db.ForeignKey('usertype.id'), nullable=False, default=3) # Default user type normal

    posts = db.relationship('Post', backref='author', lazy=True)
    comments = db.relationship('Comment', backref='author', lazy=True)

    def __repr__(self):
        return "User('{first_name}', '{last_name}', '{username}', '{email}')".format(\
        first_name=self.first_name,\
        last_name=self.last_name,\
        username=self.username,\
        email=self.email)