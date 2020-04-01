from datetime import datetime
from ascura import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_student(student_id):
    return Student.query.get(student_id)

""" @login_manager.user_loader
def load_faculty(faculty_id):
    return Faculty.query.get(faculty_id) """

class Role(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    role_name = db.Column(db.String(20), nullable=False, unique=True)
    student_role = db.relationship("Student", backref='role', lazy=True)

    def __repr__(self):
        return "Role('{id}', '{role_name}')".format(id=self.id, role_name=self.role_name)

class School(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    school_name = db.Column(db.String(5), nullable=False, unique=True)
    student_school = db.relationship("Student", backref='school', lazy=True)
    faculty_school = db.relationship("Faculty", backref='school', lazy=True)

    def __repr__(self):
        return "School('{id}', '{school_name}')".format(id=self.id, school_name=self.school_name)

class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    course_name = db.Column(db.String(7), nullable=False, unique=True)
    student_course = db.relationship("Student", backref='course', lazy=True)

    def __repr__(self):
        return "Course('{id}', '{course_name}')".format(id=self.id, course_name=self.course_name)

class SPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.now)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('student.matrix'), nullable=False)

    def __repr__(self):
        return "SPost('{title}', '{date_posted}')".format(title=self.title, date_posted=self.date_posted)

class SComment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.now)
    content = db.Column(db.Text, nullable=False)
    student_id = db.Column(db.Integer, db.ForeignKey('student.matrix'), nullable=False)

    def __repr__(self):
        return "FPost('{content}', '{date_posted}')".format(content=self.content, date_posted=self.date_posted)

class FPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.now)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('faculty.id'), nullable=False)

    def __repr__(self):
        return "FPost('{title}', '{date_posted}')".format(title=self.title, date_posted=self.date_posted)

class FComment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.now)
    content = db.Column(db.Text, nullable=False)
    faculty_id = db.Column(db.Integer, db.ForeignKey('faculty.id'), nullable=False)

    def __repr__(self):
        return "FPost('{content}', '{date_posted}')".format(content=self.content, date_posted=self.date_posted)

class Faculty(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    password = db.Column(db.String(60), nullable=False)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'), default=1)
    school_id = db.Column(db.Integer, db.ForeignKey('school.id'), nullable=False)
    short_desc = db.Column(db.String(70), nullable=False, default="Hi there, I'm new to Ascura.")
    long_desc = db.Column(db.Text, nullable=False, default="No information given.")
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    posts = db.relationship('FPost', backref='author', lazy=True)
    comments = db.relationship('FComment', backref='author', lazy=True)

    def __repr__(self):
        return "Faculty('{id}', '{first_name}', '{last_name}', '{role}', '{school}')"\
            .format(first_name=self.first_name, last_name=self.last_name, role=self.role_id, school=self.school_id)

class Student(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    matrix = db.Column(db.String(8), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'), default=1) # Done
    school_id = db.Column(db.Integer, db.ForeignKey('school.id'), nullable=False) # Done
    short_desc = db.Column(db.String(70), nullable=False, default="Hi there, I'm new to Ascura.")
    long_desc = db.Column(db.Text, nullable=False, default="No information given")
    interests = db.Column(db.String(100), nullable=False, default="This user has not specified any interests.")
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'), nullable=False) # Done
    semester = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    posts = db.relationship('SPost', backref='author', lazy=True)
    comments = db.relationship('SComment', backref='author', lazy=True)

    """ def get_id(self):
        return self.matrix.encode(encoding='UTF-8',errors='strict') """
    
    def __repr__(self):
        return "Student('{matrix}', '{first_name}', '{last_name}', '{role}', '{school}', '{course}', '{semester}')"\
            .format(matrix=self.matrix, first_name=self.first_name, last_name=self.last_name, role=self.role_id, school=self.school_id, course=self.course_id, semester=self.semester)