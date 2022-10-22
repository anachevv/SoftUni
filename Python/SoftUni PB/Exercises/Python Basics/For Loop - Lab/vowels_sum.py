user_input = input()
total_sum = 0

for x in range(0, len(user_input)):
    if user_input[x] == "a":
        total_sum += 1
    if user_input[x] == "e":
        total_sum += 2
    if user_input[x] == "i":
        total_sum += 3
    if user_input[x] == "o":
        total_sum += 4
    if user_input[x] == "u":
        total_sum += 5

print(total_sum)
