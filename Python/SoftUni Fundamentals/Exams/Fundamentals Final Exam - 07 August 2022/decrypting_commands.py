string = input()
command = input()
while command != "Finish":
    if 'Replace' in command:
        command = command.split()
        current_char, new_char = command[1], command[2]
        string = string.replace(current_char, new_char)
        print(string)
    elif 'Cut' in command:
        command = command.split()
        start_index, end_index = int(command[1]), int(command[2])
        if 0 <= start_index and end_index < len(string):
            substring = string[start_index:end_index + 1]
            string = string.replace(substring, '')
            print(string)
        else:
            print("Invalid indices!")
    elif 'Make' in command:
        command = command.split()
        letters_case = command[1]
        if letters_case == 'Upper':
            string = string.upper()
        else:
            string = string.lower()
        print(string)
    elif 'Check' in command:
        command = command.split()
        check_string = command[1]
        if check_string in string:
            print(f"Message contains {check_string}")
        else:
            print(f"Message doesn't contain {check_string}")
    elif 'Sum' in command:
        command = command.split()
        start_index, end_index = int(command[1]), int(command[2])
        if 0 <= start_index and end_index < len(string):
            substring = string[start_index:end_index + 1]
            ascii_sum = 0
            for char in substring:
                ascii_sum += ord(char)
            print(ascii_sum)
        else:
            print("Invalid indices!")
    command = input()
