def student_information():
    student_list = {}
    num = int(input("Enter the number of students: "))
    for i in range(num):
        student_id = input("Enter student ID: ")
        student_name = input("Enter student Name: ")
        student_dob = input("Enter date of birth (DD-MM-YYYY): ")
        student_list[student_id] = {'Name': student_name, 'DOB': student_dob}
    return student_list

def course_information():
    course = {}
    num_courses = int(input("Enter the number of courses: "))
    for course_num in range(1, num_courses + 1):
        course_id = input("Enter course ID: ")
        course_name = input("Enter course name: ")
        course[course_id] = {'Name': course_name}
    return course

def marks(course_dict, student_dict):
    course_id = input("Enter course ID for marks: ")

    if course_id in course_dict:
        marks_dict = {}
        for student_id, student_info in student_dict.items():
            student_name = student_info['Name']
            mark = float(input(f"Enter marks for {student_name} in {course_dict[course_id]['Name']}: "))
            if student_id not in marks_dict:
                marks_dict[student_id] = {}
            marks_dict[student_id][course_id] = mark
        return marks_dict
    else:
        print("Invalid course ID.")
        return None

def display_student_information(student_dict):
    print("\nStudent Information:")
    for student_id, info in student_dict.items():
        print(f"Student ID: {student_id}")
        print(f"Name: {info['Name']}")
        print(f"Date of Birth: {info['DOB']}")
        print("\n----------------------")

def display_course_information(course_dict):
    print("\nCourse Information:")
    for course_id, course_info in course_dict.items():
        print(f"Course ID: {course_id}")
        print(f"Course Name: {course_info['Name']}")
        print("\n----------------------")

def display_student_marks(course_dict, student_dict, marks_dict):
    print("\nStudent Marks:")
    for course_id, course_info in course_dict.items():
        print(f"\nCourse ID: {course_id}")
        print(f"Course Name: {course_info['Name']}")
        print("\nStudent Marks:")
        for student_id, student_info in student_dict.items():
            print(f"\nStudent ID: {student_id}")
            print(f"Name: {student_info['Name']}")
            if student_id in marks_dict and course_id in marks_dict[student_id]:
                mark = marks_dict[student_id][course_id]
                print(f"   Marks: {mark}")
            else:
                print("   Marks: Not available")
        print("\n----------------------")


while True:
    print("\nMain Menu:")
    print("1. Input Student Information")
    print("2. Input Course Information")
    print("3. Input Marks for selected course")
    print("4. Display Student Information")
    print("5. Display Course Information")
    print("6. Display Student Marks")
    print("0. Exit")

    choice = input("Enter your choice (0-6): ")

    if choice == "1":
        students = student_information()
    elif choice == "2":
        courses = course_information()
    elif choice == "3":
        if 'students' in locals() and 'courses' in locals():
            marks_obtained = marks(courses, students)
        else:
            print("Please enter student and course information first.")
    elif choice == "4":
        if 'students' in locals():
            display_student_information(students)
        else:
            print("Please enter student information first.")
    elif choice == "5":
        if 'courses' in locals():
            display_course_information(courses)
        else:
            print("Please enter course information first.")
    elif choice == "6":
        if 'students' in locals() and 'courses' in locals() and 'marks_obtained' in locals():
            display_student_marks(courses, students, marks_obtained)
        else:
            print("Please enter student and course information and marks first.")
    elif choice == "0":
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 0 and 6.")
