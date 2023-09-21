#Implement a function called sort_students that takes a list of student objects as input and sorts the list based on their CGPA (Cumulative Grade Point Average) in descending order. Each student object has the following attributes: name (string), roll_number (string), and cgpa (float). Test the function with different input lists of students.
def sort_students(student_list):
    sorted_students = sorted(student_list, key=lambda student: student['cgpa'], reverse=True)
    return sorted_students
students = [
    {'name': 'MUKESH', 'roll number': '22CS', 'cgpa': 9.5},
    {'name': 'SAM', 'roll number': '23CS', 'cgpa': 6.2},
    {'name': 'RAVI', 'roll number': '24CS', 'cgpa': 5.6},
] 
sorted_students = sort_students(students)
for student in sorted_students:
    print(f"Name: {student['name']},\n Roll Number: {student['roll number']},\n CGPA: {student['cgpa']}")