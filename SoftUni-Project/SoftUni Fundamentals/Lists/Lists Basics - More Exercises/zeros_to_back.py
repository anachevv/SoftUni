user_input = input().split(', ')
user_input = [int(x) for x in user_input]

for element in user_input:
    if element == 0:
        user_input.remove(element)
        user_input.append(element)

print(user_input)
