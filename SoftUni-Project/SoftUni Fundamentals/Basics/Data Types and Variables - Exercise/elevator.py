from math import ceil

n_people = int(input())
max_people = int(input())

full_courses = ceil(n_people / max_people)

print(full_courses)
