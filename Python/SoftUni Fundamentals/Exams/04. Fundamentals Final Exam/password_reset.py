string = input()
command = input()

while command != 'Done':
    command = command.split()
    if 'TakeOdd' in command:
        string = "".join([element for index, element in enumerate(string) if index % 2 != 0])
        print(string)
    elif 'Cut' in command:
        start_index, length = int(command[1]), int(command[2])
        string = string[:start_index] + string[start_index + length:]
        print(string)
    elif 'Substitute' in command:
        substring, substitute = command[1], command[2]
        if substring in string:
            string = string.replace(substring, substitute)
            print(string)
        else:
            print('Nothing to replace!')

    command = input()

print(f"Your password is: {string}")
