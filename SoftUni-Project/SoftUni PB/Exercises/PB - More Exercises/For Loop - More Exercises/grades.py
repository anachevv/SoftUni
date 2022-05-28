students = int(input())
p1 = 0
p2 = 0
p3 = 0
p4 = 0
total_grades_sum = 0

for x in range(students):
    grade = float(input())
    total_grades_sum += grade
    if grade >= 5:
        p1 += 1
    elif 4 <= grade <= 4.99:
        p2 += 1
    elif 3 <= grade <= 3.99:
        p3 += 1
    elif grade < 3:
        p4 += 1

average_score = total_grades_sum / (p1 + p2 + p3 + p4)

print(f"Top students: {p1 / (p1 + p2 + p3 + p4) * 100:.2f}%")
print(f"Between 4.00 and 4.99: {p2 / (p1 + p2 + p3 + p4) * 100:.2f}%")
print(f"Between 3.00 and 3.99: {p3 / (p1 + p2 + p3 + p4) * 100:.2f}%")
print(f"Fail: {p4 / (p1 + p2 + p3 + p4) * 100:.2f}%")
print(f"Average: {average_score:.2f}")
