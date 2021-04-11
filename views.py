import controller

def take_data_for_students():
	name = input("Enter name of student: ")
	cl = input("Class: ")
	dob = input("Enter date of birth (DD/MM/YYYY): ")
	av = float(input("Enter total score averge: "))
	hobbies = input("Enter hobbies: ")
	tchr = int(input("Enter teacher id: "))
	c = controller.Students()
	res = c.add_student(name, cl, dob, av, hobbies, tchr)
	if res:
		print("Student ", name, " has been added successfully!!")

def update_data_for_students():
	roll = int(input("Enter the roll number data to be changed: "))
	name = input("Enter name: ")
	av = float(input("Enter averge: "))
	hob = input("Enter hobbies: ")
	c = controller.Students()
	res = c.update_student(roll, name, av, hob)
	if res:
		print("Student ", name, " has been updated successfully!!")

def delete_data_from_students():
	roll = int(input("Enter the roll number data to be changed: "))
	c = controller.Students()
	res = c.delete_student(roll)
	if res:
		print("Student ", roll, " has been updated successfully!!")

def view_all_students():
	c = controller.Students()
	res = c.view_all_students()
	print("\n\n\n-------------------------------------------------------------------------------\n")
	print("Roll No. | Student Name | Student Average | Student Hobbies | Student Date of Birth")
	for student in res:
		print(student.stu_roll, " | ", student.stu_name, " | ", student.stu_average, " | ", student.stu_hobbies, " | ",\
			student.stu_dob)

def intro():
	z = 1
	while z!=5:	
		print("\n\n\n------------WELCOME TO SCHOOL DATABASE--------------------")
		print("Enter the action you want to perform: ")
		print("1. Create new student\n2. Update existing student\n3. Delete a student\n4. View all students\n5. Exit")
		z = int(input("Enter your choice (1/2/3/4/5)"))
		if z==1:
			print("\nAdding Data to student..")
			take_data_for_students()
		elif z==2:
			print("\nUpdating Data of student..")
			update_data_for_students()
		elif z==3:
			print("\nDeleting Data of student..")
			delete_data_from_students()
		elif z==4:
			print("\nViewing all students..")
			view_all_students()
		else:
			print("\nThank you for using the School Database...")

intro()