from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo

scetc_full = [('dit', 'Diploma in Information Technology'),\
        ('dcs', 'Diploma in Cyber Security'),\
        ('dtl', 'Diploma in Industrial Electrical Technology'),\
        ('dte', 'Diploma in Electrical Technology'),\
        ('ditnt', 'Diploma in Information Technology (Networking Technology)')]

class RegistrationForm(FlaskForm):
    # Matrix

	# First Name
	# Last Name
	# School
	# Course
	# Semester
	# Profile Picture

	# Email
	# Password
	# Confirm Password
    matrix = StringField('Matrix', validators=[DataRequired(), Length(min=8, max=8)])
    first_name = StringField('First Name', validators=[DataRequired(), Length(min=1, max=30)])
    last_name = StringField('Last Name', validators=[DataRequired(), Length(min=1, max=30)])
    school = SelectField('School', validators=[DataRequired()], choices=[('scet', 'School of Computing and Engineering Technology'),\
        ('sbm', 'School of Business Management'),\
        ('smart', 'School of Media Technology and Arts'),\
        ('shtm', 'School of Hospitality and Tourism Management'),\
        ('saat', 'School of Aviation and Aeronautic Technology'),\
        ('sss', 'School of Social Sciences')])
    """ scet_course = SelectField('Course', validators=[DataRequired()], choices=\
        [('dit', 'DIT'),\
        ('dcs', 'DCS'),\
        ('dtl', 'DTL'),\
        ('dte', 'DTE'),\
        ('ditnt', 'DIT (NT)')])
    sbm_course = SelectField('Course', validators=[DataRequired()], choices=\
        [('dia', 'DIA'),\
        ('difp', 'DIFP'),\
        ('dim', 'DIM'),\
        ('dk', 'DK'),\
        ('dme', 'DME'),\
        ('dsm', 'DSM')])
    adc_course = SelectField('Course', validators=[DataRequired()], choices=\
        [('dam', 'DAM'),\
        ('lme', 'LME')])
    shtm_course = SelectField('Course', validators=[DataRequired()], choices=\
        [('dca', 'DCA'),\
        ('dhm', 'DHM'),\
        ('dto', 'DTO')])
    smart_course = SelectField('Course', validators=[DataRequired()], choices=\
        [('dmm', 'DMM'),\
        ('dta', 'DTA'),\
        ('dtm', 'DTM'),\
        ('dts', 'DTS')])
    sss_course = SelectField('Course', validators=[DataRequired()], choices=\
        [('dbk', 'DBK'),\
        ('dpk', 'DPK')]) """
    course = StringField('Course', validators=[DataRequired(), Length(min=2, max=7)])
    semester = StringField('Semester', validators=[DataRequired(), Length(min=1, max=2)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')
