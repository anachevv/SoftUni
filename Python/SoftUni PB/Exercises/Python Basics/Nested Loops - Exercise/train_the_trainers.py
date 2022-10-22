jury = int(input())
presentation_name = input()

presentation_grade_sum = 0
total_grade_sum = 0
grade_counter = 0

while presentation_name != "Finish":

    for grades in range(jury):
        grade = float(input())
        grade_counter += 1
        presentation_grade_sum += grade
        total_grade_sum += grade

    print(f"{presentation_name} - {presentation_grade_sum / jury:.2f}.")

    presentation_grade_sum = 0
    presentation_name = input()

print(f"Student's final assessment is {total_grade_sum / grade_counter:.2f}.")
