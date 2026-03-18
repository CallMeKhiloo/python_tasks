file_students = open('students.txt', 'w')
file_grades = open('grades.txt', 'w')

file_students.write("1,Ahmed Ali\n2,Sara Mohamed\n3,John Doe\n4,Jane Smith")
file_grades.write("1,Python,85\n2,Math,90\n3,Python,78\n4,Math,92\n1,Math,88\n2,Python,95\n3,Math,80\n4,Python,91")

file_students.close()
file_grades.close()
