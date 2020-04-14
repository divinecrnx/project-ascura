from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from ascura.models import User

class SCETRegistrationForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired(), Length(min=1, max=30)])
    last_name = StringField('Last Name', validators=[DataRequired(), Length(min=1, max=30)])
    username = StringField('Username', validators=[DataRequired(), Length(min=3, max=14)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    course = SelectField('Course', validators=[DataRequired()], choices=\
        [('1', 'DIT'),\
        ('2', 'DCS'),\
        ('3', 'DTL'),\
        ('4', 'DTE'),\
        ('5', 'DIT (NT)')])
    semester = SelectField('Semester', validators=[DataRequired()], choices=\
        [('1', '1'),\
        ('2', '2'),\
        ('3', '3'),\
        ('4', '4'),\
        ('5', '5'),\
        ('6', '6'),\
        ('6+', '6+')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken. Please choose a different one.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is taken. Please choose a different one.')

class SMARTRegistrationForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired(), Length(min=1, max=30)])
    last_name = StringField('Last Name', validators=[DataRequired(), Length(min=1, max=30)])
    username = StringField('Username', validators=[DataRequired(), Length(min=3, max=14)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    course = SelectField('Course', validators=[DataRequired()], choices=\
        [('6', 'DMM'),\
        ('7', 'DTA'),\
        ('8', 'DTM'),\
        ('9', 'DTS')])
    semester = SelectField('Semester', validators=[DataRequired()], choices=\
        [('1', '1'),\
        ('2', '2'),\
        ('3', '3'),\
        ('4', '4'),\
        ('5', '5'),\
        ('6', '6'),\
        ('6+', '6+')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken. Please choose a different one.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is taken. Please choose a different one.')

class SBMRegistrationForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired(), Length(min=1, max=30)])
    last_name = StringField('Last Name', validators=[DataRequired(), Length(min=1, max=30)])
    username = StringField('Username', validators=[DataRequired(), Length(min=3, max=14)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    course = SelectField('Course', validators=[DataRequired()], choices=\
        [('10', 'DIA'),\
        ('11', 'DIFP'),\
        ('12', 'DIM'),\
        ('13', 'DK'),\
        ('14', 'DME'),\
        ('15', 'DSM')])
    semester = SelectField('Semester', validators=[DataRequired()], choices=\
        [('1', '1'),\
        ('2', '2'),\
        ('3', '3'),\
        ('4', '4'),\
        ('5', '5'),\
        ('6', '6'),\
        ('6+', '6+')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken. Please choose a different one.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is taken. Please choose a different one.')

class SHTMRegistrationForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired(), Length(min=1, max=30)])
    last_name = StringField('Last Name', validators=[DataRequired(), Length(min=1, max=30)])
    username = StringField('Username', validators=[DataRequired(), Length(min=3, max=14)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    course = SelectField('Course', validators=[DataRequired()], choices=\
        [('16', 'DCA'),\
        ('17', 'DHM'),\
        ('18', 'DTO')])
    semester = SelectField('Semester', validators=[DataRequired()], choices=\
        [('1', '1'),\
        ('2', '2'),\
        ('3', '3'),\
        ('4', '4'),\
        ('5', '5'),\
        ('6', '6'),\
        ('6+', '6+')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken. Please choose a different one.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is taken. Please choose a different one.')

class SAATRegistrationForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired(), Length(min=1, max=30)])
    last_name = StringField('Last Name', validators=[DataRequired(), Length(min=1, max=30)])
    username = StringField('Username', validators=[DataRequired(), Length(min=3, max=14)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    course = SelectField('Course', validators=[DataRequired()], choices=\
        [('19', 'DAM'),\
        ('20', 'LME')])
    semester = SelectField('Semester', validators=[DataRequired()], choices=\
        [('1', '1'),\
        ('2', '2'),\
        ('3', '3'),\
        ('4', '4'),\
        ('5', '5'),\
        ('6', '6'),\
        ('6+', '6+')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken. Please choose a different one.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is taken. Please choose a different one.')

class SSSRegistrationForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired(), Length(min=1, max=30)])
    last_name = StringField('Last Name', validators=[DataRequired(), Length(min=1, max=30)])
    username = StringField('Username', validators=[DataRequired(), Length(min=3, max=14)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    course = SelectField('Course', validators=[DataRequired()], choices=\
        [('21', 'DBK'),\
        ('22', 'DPK')])
    semester = SelectField('Semester', validators=[DataRequired()], choices=\
        [('1', '1'),\
        ('2', '2'),\
        ('3', '3'),\
        ('4', '4'),\
        ('5', '5'),\
        ('6', '6'),\
        ('6+', '6+')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken. Please choose a different one.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is taken. Please choose a different one.')

class FacultyRegistrationForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired(), Length(min=1, max=30)])
    last_name = StringField('Last Name', validators=[DataRequired(), Length(min=1, max=30)])
    username = StringField('Username', validators=[DataRequired(), Length(min=3, max=14)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    role = SelectField('Role', validators=[DataRequired()], choices=\
        [('4', 'Lecturer'),\
        ('5', 'HOP'),\
        ('6', 'Dean')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken. Please choose a different one.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is taken. Please choose a different one.')

class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

class UpdateStudentProfileForm(FlaskForm):
    short_desc = StringField('Short description')
    long_desc = TextAreaField('Long description')
    interests = StringField('Interests')
    picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Update profile')

    def validate_short_desc(self, short_desc):
        limit = 70
        if len(short_desc.data) > limit:
            raise ValidationError('Your description was too long. Try again with less than ' + str(limit) + ' words.')

    def validate_long_desc(self, long_desc):
        limit = 450
        if len(long_desc.data) > limit:
            raise ValidationError('Your description was too long. People are likely to read your description if it was a bit shorter. Try again with less than ' + str(limit) + ' words.')

    def validate_interests(self, interests):
        limit = 100
        if len(interests.data) > limit:
            raise ValidationError('You specified too many interests. Please keep them short and brief and with less than ' + str(limit) + ' characters.')

class UpdateStudentAccountForm(FlaskForm):
    semester = SelectField('Semester', validators=[DataRequired()], choices=\
        [('1', '1'),\
        ('2', '2'),\
        ('3', '3'),\
        ('4', '4'),\
        ('5', '5'),\
        ('6', '6'),\
        ('6+', '6+')])
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Update account')

    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('That email is taken. Please choose a different one.')

class UpdateFacultyAccountForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Update account')

    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('That email is taken. Please choose a different one.')

class UpdateStudentPasswordForm(FlaskForm):
    old_password = PasswordField('Old password')
    password = PasswordField('New password')
    confirm_password = PasswordField('Confirm new password', validators=[EqualTo('password')])
    submit = SubmitField('Update password')

class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    submit = SubmitField('Post')

class CommentForm(FlaskForm):
    content = TextAreaField('Content', validators=[DataRequired()])
    submit = SubmitField('Submit')
