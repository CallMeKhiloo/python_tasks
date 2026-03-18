from utils import read_file

def display_students():
    students = read_file('students.txt')
    students = students.split('\n')
    for student in students:
        print(student.split(',')[1])

def display_python_grades():
    grades = read_file('grades.txt').split('\n')
    for grade in grades:
        grade_info = grade.split(',')
        if grade_info[1] == 'Python':
            print(f"student ID: {grade_info[0]} has grade: {grade_info[2]}")

def print_student_grades(student_id):
    grades = read_file('grades.txt').split('\n')
    cntr = 0
    for grade in grades:
        grade_info = grade.split(',')
        if grade_info[0] == student_id:
            cntr += 1
            print(f"student ID: {grade_info[0]} has grade: {grade_info[2]} in {grade_info[1]}")
    if cntr == 0:
        print("ID is not found.")

def print_average_grade():
    students_info = {}
    students = read_file('students.txt')
    students = students.split('\n')
    for student in students:
        student_info = student.split(',')
        students_info[student_info[0]] = (student_info[1], 0, 0)
    grades = read_file('grades.txt').split('\n')
    for grade in grades:
        grade_info = grade.split(',')
        students_info[grade_info[0]] = (students_info[grade_info[0]][0], students_info[grade_info[0]][1] + int(grade_info[2]), students_info[grade_info[0]][2] + 1)
    for key, value in students_info.items():
        print(f"{value[0]} with ID: {key} has average grade: {value[1] / value[2]}")


display_students()
print("---------------------------")
display_python_grades()
print("---------------------------")
id = input("If you want to display all the grades of a specific student, please enter the student ID(if not just press enter):")
if id.isdigit():
    print_student_grades(id)
else:
    print("No student ID entered, exiting...")
print("---------------------------")
print_average_grade()