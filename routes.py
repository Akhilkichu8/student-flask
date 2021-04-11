from flask import Flask, render_template, request
import controller

app = Flask(__name__)

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/add_student", methods=["POST", "GET"])
def add_student():
	if request.method == "POST":
		result = request.form
		c = controller.Students()
		res = c.add_student(result["txt_name"], result["txt_class"], result["txt_dob"], \
			float(result["txt_average"]), result["txt_hobbies"], int(result["txt_teacher"]))
		return render_template("index.html")
	return render_template("add_student.html")

@app.route("/view_students")
def view_all():
	c = controller.Students()
	res = c.view_all_students()
	return render_template("view_students.html", students=res)

@app.route("/delete_stu",methods=["POST", "GET"])
def delete_data_from_students():
	if request.method == "POST":
		result = request.form
		c = controller.Students()
		res = c.delete_student(int(result["ROLL_NUMBER"]))
		return render_template("index.html")
	return render_template("delete_stu.html")



if __name__ == "__main__":
	app.run(debug = True)
