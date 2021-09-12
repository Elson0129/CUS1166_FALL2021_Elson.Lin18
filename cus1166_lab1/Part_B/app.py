from myModules.models import *
from myModules.math_utils import *

def main():
    roster = []
    rosterSize = input("How many students are in this roster? ")
    print("Please enter information for " + rosterSize + " students")

    for i in range(int(rosterSize)):
        name = input("Enter Student " + str(i + 1) + "'s Name: ")
        grade = input("Enter Student " + str(i + 1) + "'s Grade: ")
        grade = int(grade)
        student = Student(name,grade)
        roster.append(student)

    for student in roster:
        student.print_student_info();
    print("The average grade for the roster: {:.2f}".format(average_grade(roster)))

main()
