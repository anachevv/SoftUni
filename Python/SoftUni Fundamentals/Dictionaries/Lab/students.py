user_input = input()
courses = {}

while ':' in user_input:
    text = user_input.split(':')
    student_name = text[0]
    student_id = text[1]
    student_course = text[2]

    if student_course not in courses.keys():
        courses[student_course] = {}
    courses[student_course][student_id] = student_name

    user_input = input()

user_input = user_input.replace('_', ' ')

for id in courses[user_input]:
    print(f'{courses[user_input][id]} - {id}')
