student_marks={
    'Alice': 85,
    'Bob': 75,
    'Charlie':80
}
student_name = input("Enter Your Student's Name :");
if student_name in student_marks:
    print(f"{student_name} marks: {student_marks[student_name]}")
else:
    print("Student Not Found")