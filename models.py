from sqlalchemy import Column, DateTime, String, Integer, ForeignKey, func, Float, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base
from datetime import date


Base = declarative_base()

class Teacher(Base):
	__tablename__ = "teachers"
	tch_id = Column(Integer, primary_key=True)
	tch_name = Column(String, nullable=False)
	tch_subject = Column(String)
	tch_salary = Column(Float)

class Student(Base):
	__tablename__ = "students"
	stu_roll = Column(Integer, primary_key=True)
	stu_name = Column(String, nullable=False)
	stu_class = Column(String)
	stu_dob = Column(DateTime)
	stu_average = Column(Float)
	stu_hobbies = Column(String)
	stu_class_teacher = Column(Integer)
	# stu_class_teacher = Column(Integer, ForeignKey("teachers.tch_id"))
	# teacher = relationship("Teacher", back_populates="tch_students")

	def __repr__(self):
		return "<Teacher(teacher_name='%s')>" % self.stu_class_teacher

engine = create_engine('sqlite:///school.db', echo=False)
session = sessionmaker()
session.configure(bind=engine)
Base.metadata.create_all(engine)
s = session()


def add_student(name, cl,  dob, av, hob, tch):
	student = Student(stu_name=name, stu_class=cl, stu_dob=dob, stu_average=av, stu_hobbies=hob, stu_class_teacher=tch)
	s.add(student)
	s.commit()
	return True

def update_student(roll, name, av, hobbies):
	std = s.query(Student).filter_by(stu_roll=roll).first()
	std.stu_hobbies = hobbies
	std.stu_name = name
	std.stu_average = av
	s.commit()
	return True

def delete_student(roll):
	std = s.query(Student).filter_by(stu_roll=roll).first()
	s.delete(std)
	s.commit()
	return True

def view_student(roll):
	std = s.query(Student).filter_by(stu_roll=roll).first()
	return std

def view_all_students():
	studs = s.query(Student)
	return  studs

# for e in view_all_students():
# 	print(e.stu_class_teacher)



# def add_teacher(name, subject, salary):
# 	teacher = Teacher(tch_name=name, tch_subject=subject, tch_salary=salary)
# 	s.add(teacher)
# 	s.commit()
# 	return True
