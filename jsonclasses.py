import json


#POP QUIZ CLASS
class Student:
	def __init__(self, name, grade):
		self.name = name
		self.grade = grade

	def intro(self):
		print "Hello my name is %s and my grade is %d" %(self.name, self.grade)

class Teacher:
	class_average = None
	def __init__(self, name, course, students):
		self.name = name
		self.course = course
		self.students = students

	def intro(self):
		print "Hello my name is %s and I teach %s." %(self.name, self.course)
		student_string = ""
		for student in self.students:
			student_string += student.name + " "
		print "My students are %s" %(student_string)

	#POP QUIZ METHOD
	def calculate_class_average(self):
		average = 0.0
		for student in self.students:
			average += student.grade
		self.class_average = average / len(self.students)

def parse_json():
	file = open('example.json', 'r')
	json_string = file.read()
	parsed_json = json.loads(json_string)
	students = parsed_json["students"]
	student_list = []
	for student in students:
		student_list.append(Student(student["name"], student["grade"]))
	return student_list

student_list = parse_json()

ex = Teacher("Mr. Bob", "English", student_list)
ex.intro()
ex.calculate_class_average()
print ex.class_average

