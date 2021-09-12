class Student:
    def __init__(self, studentName, studentGrade):
        self.studentName = studentName
        self.studentGrade = studentGrade

    def set_grade(self, grade):
        self.studentGrade = grade

    def get_grade(self):
        return self.studentGrade

    def print_student_info(self):
        print("Student: {}, Grade: {}".format(self.studentName, self.studentGrade))
