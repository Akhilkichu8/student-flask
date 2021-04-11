import models
from datetime import datetime

class Students:
	def add_student(self, name, cl, dob, av, hobbies, tchr):
		correct = datetime.strptime(dob, "%Y-%m-%d")
		dob = correct.date()
		res = models.add_student(name, cl, dob, av, hobbies, tchr)
		return res

	def update_student(self, roll, name, av, hobbies):
		res = models.update_student(roll, name, av, hobbies)
		return res

	def delete_student(self, roll):
		res = models.delete_student(roll)
		return res

	def view_all_students(self):
		res = models.view_all_students()
		return res