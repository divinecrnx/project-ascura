from ascura import db
from ascura.models import Role, School, Course, SPost, SComment, FPost, FComment, Faculty, Student

db.create_all() # Create database

# role_unspecified = Role(role_name="Unspecified")
role_student = Role(role_name="Student")
role_vice_chairman = Role(role_name="Vice Chairman")
role_chairman = Role(role_name="Chairman")
role_lecturer = Role(role_name="Lecturer")
role_hop = Role(role_name="HOP")
role_dean = Role(role_name="Dean")


school_scet = School(school_name="SCET")
school_smart = School(school_name="SMART")
school_sbm = School(school_name="SBM")
school_shtm = School(school_name="SHTM")
school_saat = School(school_name="SAAT")
school_sss = School(school_name="SSS")

course_dit = Course(course_name="DIT")
course_dcs = Course(course_name="DCS")
course_dtl = Course(course_name="DTL")
course_dte = Course(course_name="DTE")
course_ditnt = Course(course_name="DIT(NT)")

course_dmm = Course(course_name="DMM")
course_dta = Course(course_name="DTA")
course_dtm = Course(course_name="DTM")
course_dts = Course(course_name="DTS")

course_dia = Course(course_name="DIA")
course_difp = Course(course_name="DIFP")
course_dim = Course(course_name="DIM")
course_dk = Course(course_name="DK")
course_dme = Course(course_name="DME")
course_dsm = Course(course_name="DSM")

course_dca = Course(course_name="DCA")
course_dhm = Course(course_name="DHM")
course_dto = Course(course_name="DTO")

course_dam = Course(course_name="DAM")
course_lme = Course(course_name="LME")

course_dbk = Course(course_name="DBK")
course_dpk = Course(course_name="DPK")

""" student_1 = Student(matrix="T0000404", password="password",\
    first_name="Zulhilmi", last_name="Abdul Rasheed",\
    role_id=3, school_id=1, course_id=1, semester=5,\
    email="zulhilmi.rasheed98@gmail.com") """

# post_1 = SPost(title="First student post", content="First student post content", user_id=x.matrix)

db.session.add(role_student)
db.session.add(role_vice_chairman)
db.session.add(role_chairman)
db.session.add(role_lecturer)
db.session.add(role_hop)
db.session.add(role_dean)

db.session.add(school_scet)
db.session.add(school_smart)
db.session.add(school_sbm)
db.session.add(school_shtm)
db.session.add(school_saat)
db.session.add(school_sss)

db.session.add(course_dit)
db.session.add(course_dcs)
db.session.add(course_dtl)
db.session.add(course_dte)
db.session.add(course_ditnt)

db.session.add(course_dmm)
db.session.add(course_dta)
db.session.add(course_dtm)
db.session.add(course_dts)

db.session.add(course_dia)
db.session.add(course_difp)
db.session.add(course_dim)
db.session.add(course_dk)
db.session.add(course_dme)
db.session.add(course_dsm)

db.session.add(course_dca)
db.session.add(course_dhm)
db.session.add(course_dto)

db.session.add(course_dam)
db.session.add(course_lme)

db.session.add(course_dbk)
db.session.add(course_dpk)

# db.session.add(post_1)
# db.session.add(student_1)

db.session.commit()