n_students = int(input())
students_and_grades = {}

for _ in range(n_students):
    student_name = input()
    grade = float(input())

    if student_name not in students_and_grades:
        students_and_grades[student_name] = []
    students_and_grades[student_name].append(grade)

for name, grade in students_and_grades.items():
    average_grade = sum(students_and_grades[name]) / len(students_and_grades[name])
    if average_grade >= 4.5:
        print(f"{name} -> {average_grade:.2f}")
