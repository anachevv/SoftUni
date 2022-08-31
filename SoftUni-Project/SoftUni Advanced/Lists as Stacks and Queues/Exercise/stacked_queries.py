stack = []
n_commands = int(input())
for _ in range(n_commands):
    command = input()
    if len(command) > 1:
        number = int(command.split()[1])
        stack.append(number)
    else:
        if command == "2" and stack:
            stack.pop()
        elif command == "3":
            max_number = -100000
            for number in stack:
                if number > max_number:
                    max_number = number
            print(max_number)
        elif command == "4":
            min_number = 100000
            for number in stack:
                if number < min_number:
                    min_number = number
            print(min_number)
reversed_list = []
while stack:
    reversed_list.append(stack.pop())

reversed_stack = ", ".join(str(num) for num in reversed_list)
print(reversed_stack)
