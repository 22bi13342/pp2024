import math
import numpy as np

class Student:
    def __init__(self, student_id, name, dob):
        self.student_id = student_id
        self.name = name
        self.dob = dob

class Course:
    def __init__(self, course_id, name, credits):
        self.course_id = course_id
        self.name = name
        self.credits = credits

class MarkSheet:
    def __init__(self):
        self.students = {}
        self.courses = {}
        self.marks = {}

    def add_student(self, student_id, name, dob):
        self.students[student_id] = Student(student_id, name, dob)

    def add_course(self, course_id, name, credits):
        self.courses[course_id] = Course(course_id, name, credits)

    def add_marks(self, student_id, course_id, marks):
        if student_id not in self.marks:
            self.marks[student_id] = {}
        self.marks[student_id][course_id] = math.floor(marks)

    def calculate_gpa(self, student_id):
        if student_id in self.marks:
            total_credits = 0
            total_weighted_marks = 0
            for course_id, marks in self.marks[student_id].items():
                course = self.courses[course_id]
                total_credits += course.credits
                total_weighted_marks += course.credits * marks
            if total_credits == 0:
                return 0
            else:
                return total_weighted_marks / total_credits
        else:
            return 0

    def display_student_information(self):
        print("\nStudent Information:")
        for student_id, student in self.students.items():
            print(f"Student ID: {student.student_id}")
            print(f"Name: {student.name}")
            print(f"Date of Birth: {student.dob}")
            print("\n----------------------")

    def display_course_information(self):
        print("\nCourse Information:")
        for course_id, course in self.courses.items():
            print(f"Course ID: {course.course_id}")
            print(f"Course Name: {course.name}")
            print(f"Credits: {course.credits}")
            print("\n----------------------")

    def display_student_marks(self):
        print("\nStudent Marks:")
        for student_id, student in self.students.items():
            print(f"\nStudent ID: {student.student_id}")
            print(f"Name: {student.name}")
            print("Marks:")
            if student_id in self.marks:
                for course_id, marks in self.marks[student_id].items():
                    course_name = self.courses[course_id].name
                    print(f"Course: {course_name}, Marks: {marks}")
            else:
                print("No marks available")
            print("\n----------------------")

    def display_student_gpa(self):
        print("\nStudent GPA:")
        for student_id, student in self.students.items():
            gpa = self.calculate_gpa(student_id)
            print(f"Student ID: {student.student_id}")
            print(f"Name: {student.name}")
            print(f"GPA: {gpa}")
            print("\n----------------------")

    def sort_students_by_gpa(self):
        sorted_students = sorted(self.students.values(), key=lambda x: self.calculate_gpa(x.student_id), reverse=True)
        print("\nStudents Sorted by GPA:")
        for student in sorted_students:
            gpa = self.calculate_gpa(student.student_id)
            print(f"Student ID: {student.student_id}")
            print(f"Name: {student.name}")
            print(f"GPA: {gpa}")
            print("\n----------------------")

mark_sheet = MarkSheet()

while True:
    print("\nMain Menu:")
    print("1. Input Student Information")
    print("2. Input Course Information")
    print("3. Input Marks for selected course")
    print("4. Display Student Information")
    print("5. Display Course Information")
    print("6. Display Student Marks")
    print("7. Calculate and Display Student GPA")
    print("8. Sort Students by GPA")
    print("0. Exit")

    choice = input("Enter your choice (0-8): ")

    if choice == "1":
        student_id = input("Enter student ID: ")
        name = input("Enter student Name: ")
        dob = input("Enter date of birth (DD-MM-YYYY): ")
        mark_sheet.add_student(student_id, name, dob)
    elif choice == "2":
        course_id = input("Enter course ID: ")
        name = input("Enter course name: ")
        credits = int(input("Enter course credits: "))
        mark_sheet.add_course(course_id, name, credits)
    elif choice == "3":
        student_id = input("Enter student ID: ")
        course_id = input("Enter course ID: ")
        marks = float(input("Enter marks for the student: "))
        mark_sheet.add_marks(student_id, course_id, marks)
    elif choice == "4":
        mark_sheet.display_student_information()
    elif choice == "5":
        mark_sheet.display_course_information()
    elif choice == "6":
        mark_sheet.display_student_marks()
    elif choice == "7":
        mark_sheet.display_student_gpa()
    elif choice == "8":
        mark_sheet.sort_students_by_gpa()
    elif choice == "0":
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 0 and 8.")
