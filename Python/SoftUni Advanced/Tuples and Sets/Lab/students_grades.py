n_people = int(input())
info = {}
for _ in range(n_people):
    current_info = input().split()
    student, grade = current_info[0], float(current_info[1])
    if student not in info:
        info[student] = []
    info[student] += [grade]

for student, grade in info.items():
    avg_grade = sum(grade) / len(grade)
    print(f"{student} -> {' '.join(f'{x:.2f}' for x in grade)} (avg: {avg_grade:.2f})")
