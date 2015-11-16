class Student(object):
    def __init__(self, name, major, GPA, courses):
        self.name = name
        self.major = major
        self.gpa = 0
        self.courses = courses

    def enroll(self, course):
        self.courses.append(course)

    def drop(self, course):
        self.courses.remove(course)
          
    def introduction(self):
        print "Hello! My name is %s, and I'm a %s major. My GPA is %s." % (self.name, self.major, self.gpa)

    def print_courses(self):
        course_string = ""
        for course in self.courses:
            course_string += course + ','
        print "Hello! I am taking " + course_string[:len(course_string)-1] + "!"

    def calculate_GPA(self, grades):
        grades_dict = {"A" : 4, "B" : 3, "C" : 2, "D" : 1, "F" : 0}
        sum = 0
        for grade in grades:
            grade = grade[:1]
            sum += grades_dict[grade]
        self.gpa = sum / float(len(grades))
