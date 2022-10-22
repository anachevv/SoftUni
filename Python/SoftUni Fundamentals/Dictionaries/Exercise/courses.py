command = input()
courses_and_students = {}

while command != 'end':
    course, student = command.split(' : ')
    if course not in courses_and_students:
        courses_and_students[course] = []
    courses_and_students[course].append(student)

    command = input()

for course, student in courses_and_students.items():
    print(f"{course}: {len(courses_and_students[course])}", end="\n-- ")
    print("\n-- ".join(student))
