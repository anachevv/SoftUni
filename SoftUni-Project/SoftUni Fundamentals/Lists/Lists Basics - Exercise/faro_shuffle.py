user_input = input().split()
shuffles_count = int(input())

for shuffle in range(shuffles_count):
    lst = []

    middle = len(user_input) // 2
    left_part = user_input[:middle]
    right_part = user_input[middle:]

    for index in range(len(left_part)):
        lst.append(left_part[index])
        lst.append(right_part[index])

    user_input = lst

print(user_input)
