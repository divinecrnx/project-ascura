from ascura import db
from ascura.models import Role, School, Course, SPost, SComment, FPost, FComment, Faculty, Student

db.create_all() # Create database

role_unspecified = Role(role_name="Unspecified")
role_student = Role(role_name="Student")
role_chairman = Role(role_name="Chairman")

school_scet = School(school_name="SCET")
school_smart = School(school_name="SMART")
school_sbm = School(school_name="SBM")
school_shtm = School(school_name="SHTM")
school_saat = School(school_name="SAAT")
school_sss = School(school_name="SSS")

course_dit = Course(course_name="DIT")

student_1 = Student(matrix="T0000404", password="password",\
    first_name="Zulhilmi", last_name="Abdul Rasheed",\
    role_id=3, school_id=1, course_id=1, semester=5,\
    email="zulhilmi.rasheed98@gmail.com")

post_1 = SPost(title="First student post", content="First student post content", user_id=x.matrix)

db.session.add(role_unspecified)
db.session.add(role_student)
db.session.add(role_chairman)
db.session.add(school_scet)
db.session.add(school_smart)
db.session.add(school_sbm)
db.session.add(school_shtm)
db.session.add(school_saat)
db.session.add(school_sss)
db.session.add(course_dit)
db.session.add(post_1)
db.session.add(student_1)

db.session.commit()