student_name = input()
year = 1
count = 0
total_sum = 0

while year <= 12:
    if count > 1:
        break

    grade = float(input())

    if grade < 4:
        count += 1
        continue

    total_sum += grade

    year += 1

if count > 1:
    print(f"{student_name} has been excluded at {year} grade")
else:
    average_sum = total_sum / 12
    print(f"{student_name} graduated. Average grade: {average_sum:.2f}")
