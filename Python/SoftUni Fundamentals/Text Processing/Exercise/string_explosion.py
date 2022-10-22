string = input()
strength = 0
result = ""

for index in range(len(string)):
    if strength > 0 and string[index] != '>':
        strength -= 1
    elif string[index] == '>':
        strength += int(string[index + 1])
        result += string[index]
    else:
        result += string[index]

print(result)
