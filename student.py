class Student(object):
    gpa = None
    courses = None
    def __init__(self, name, major):
        self.name = name
        self.major = major

    def enroll(self, *courses):
        if(self.courses == None):
            self.courses = []
        for course in courses:
            self.courses.append(course)
        print "My courses are %s" % ', '.join(self.courses)

    def drop(self, *courses):
        if(self.courses == None):
            self.courses = []
        for course in courses:
            self.courses.remove(course)

    def introduction(self):
        print "My name is %s, and I'm a %s major. My GPA is %s." % (self.name, self.major, "nothing because I haven't taken any classes yet" if(self.gpa == None) else self.gpa)

    def print_courses(self):
        if(self.courses == None):
            print "I'm not taking any courses."
            return
        course_string = ""
        for course in self.courses:
            course_string += course + ','
        print "I am taking " + ', '.join(self.courses) + "!"

    def calculate_GPA(self, grades):
        grades_dict = {"A" : 4, "B" : 3, "C" : 2, "D" : 1, "F" : 0}
        sum = 0
        for grade in grades:
            grade = grade[:1]
            sum += grades_dict[grade]
        self.gpa = sum / float(len(grades))
        print "My GPA is %s!" % self.gpa

gabe = Student("Gabe", "CS")
gabe.introduction()
gabe.calculate_GPA(['A','B','C'])
gabe.enroll("English", "Math")
gabe.print_courses()
