from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from ascura.models import Student

""" scetc_full = [('dit', 'Diploma in Information Technology'),\
        ('dcs', 'Diploma in Cyber Security'),\
        ('dtl', 'Diploma in Industrial Electrical Technology'),\
        ('dte', 'Diploma in Electrical Technology'),\
        ('ditnt', 'Diploma in Information Technology (Networking Technology)')] """

class SCETRegistrationForm(FlaskForm):
    matrix = StringField('Matrix', validators=[DataRequired(), Length(min=8, max=8)])
    first_name = StringField('First Name', validators=[DataRequired(), Length(min=1, max=30)])
    last_name = StringField('Last Name', validators=[DataRequired(), Length(min=1, max=30)])
    course = SelectField('Course', validators=[DataRequired()], choices=\
        [('1', 'DIT'),\
        ('2', 'DCS'),\
        ('3', 'DTL'),\
        ('4', 'DTE'),\
        ('5', 'DIT (NT)')])
    semester = StringField('Semester', validators=[DataRequired(), Length(min=1, max=2)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_matrix(self, matrix):
        user = Student.query.filter_by(matrix=matrix.data).first()
        if user:
            raise ValidationError('That matrix is taken. Please contact the site admin if this is a mistake.')

    def validate_email(self, email):
        user = Student.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is taken. Please choose a different one.')

class SMARTRegistrationForm(FlaskForm):
    matrix = StringField('Matrix', validators=[DataRequired(), Length(min=8, max=8)])
    first_name = StringField('First Name', validators=[DataRequired(), Length(min=1, max=30)])
    last_name = StringField('Last Name', validators=[DataRequired(), Length(min=1, max=30)])
    course = SelectField('Course', validators=[DataRequired()], choices=\
        [('6', 'DMM'),\
        ('7', 'DTA'),\
        ('8', 'DTM'),\
        ('9', 'DTS')])
    semester = StringField('Semester', validators=[DataRequired(), Length(min=1, max=2)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_matrix(self, matrix):
        user = Student.query.filter_by(matrix=matrix.data).first()
        if user:
            raise ValidationError('That matrix is taken. Please contact the site admin if this is a mistake.')

    def validate_email(self, email):
        user = Student.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is taken. Please choose a different one.')

class SBMRegistrationForm(FlaskForm):
    matrix = StringField('Matrix', validators=[DataRequired(), Length(min=8, max=8)])
    first_name = StringField('First Name', validators=[DataRequired(), Length(min=1, max=30)])
    last_name = StringField('Last Name', validators=[DataRequired(), Length(min=1, max=30)])
    course = SelectField('Course', validators=[DataRequired()], choices=\
        [('10', 'DIA'),\
        ('11', 'DIFP'),\
        ('12', 'DIM'),\
        ('13', 'DK'),\
        ('14', 'DME'),\
        ('15', 'DSM')])
    semester = StringField('Semester', validators=[DataRequired(), Length(min=1, max=2)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_matrix(self, matrix):
        user = Student.query.filter_by(matrix=matrix.data).first()
        if user:
            raise ValidationError('That matrix is taken. Please contact the site admin if this is a mistake.')

    def validate_email(self, email):
        user = Student.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is taken. Please choose a different one.')

class SHTMRegistrationForm(FlaskForm):
    matrix = StringField('Matrix', validators=[DataRequired(), Length(min=8, max=8)])
    first_name = StringField('First Name', validators=[DataRequired(), Length(min=1, max=30)])
    last_name = StringField('Last Name', validators=[DataRequired(), Length(min=1, max=30)])
    course = SelectField('Course', validators=[DataRequired()], choices=\
        [('16', 'DCA'),\
        ('17', 'DHM'),\
        ('18', 'DTO')])
    semester = StringField('Semester', validators=[DataRequired(), Length(min=1, max=2)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_matrix(self, matrix):
        user = Student.query.filter_by(matrix=matrix.data).first()
        if user:
            raise ValidationError('That matrix is taken. Please contact the site admin if this is a mistake.')

    def validate_email(self, email):
        user = Student.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is taken. Please choose a different one.')

class SAATRegistrationForm(FlaskForm):
    matrix = StringField('Matrix', validators=[DataRequired(), Length(min=8, max=8)])
    first_name = StringField('First Name', validators=[DataRequired(), Length(min=1, max=30)])
    last_name = StringField('Last Name', validators=[DataRequired(), Length(min=1, max=30)])
    course = SelectField('Course', validators=[DataRequired()], choices=\
        [('19', 'DAM'),\
        ('20', 'LME')])
    semester = StringField('Semester', validators=[DataRequired(), Length(min=1, max=2)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_matrix(self, matrix):
        user = Student.query.filter_by(matrix=matrix.data).first()
        if user:
            raise ValidationError('That matrix is taken. Please contact the site admin if this is a mistake.')

    def validate_email(self, email):
        user = Student.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is taken. Please choose a different one.')

class SSSRegistrationForm(FlaskForm):
    matrix = StringField('Matrix', validators=[DataRequired(), Length(min=8, max=8)])
    first_name = StringField('First Name', validators=[DataRequired(), Length(min=1, max=30)])
    last_name = StringField('Last Name', validators=[DataRequired(), Length(min=1, max=30)])
    course = SelectField('Course', validators=[DataRequired()], choices=\
        [('21', 'DBK'),\
        ('22', 'DPK')])
    semester = StringField('Semester', validators=[DataRequired(), Length(min=1, max=2)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_matrix(self, matrix):
        user = Student.query.filter_by(matrix=matrix.data).first()
        if user:
            raise ValidationError('That matrix is taken. Please contact the site admin if this is a mistake.')

    def validate_email(self, email):
        user = Student.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is taken. Please choose a different one.')

class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')
