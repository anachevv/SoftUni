sequence_of_letters_and_numbers = input()
command = input()

while command != 'Generate':
    command = command.split('>>>')
    if 'Contains' in command:
        substring = command[1]
        if substring in sequence_of_letters_and_numbers:
            print(f"{sequence_of_letters_and_numbers} contains {substring}")
        else:
            print("Substring not found!")
    elif 'Flip' in command:
        case, start_index, end_index = command[1], int(command[2]), int(command[3])
        part = sequence_of_letters_and_numbers[start_index:end_index]
        if case == 'Upper':
            sequence_of_letters_and_numbers = sequence_of_letters_and_numbers.replace(part, part.upper())
        else:
            sequence_of_letters_and_numbers = sequence_of_letters_and_numbers.replace(part, part.lower())
        print(sequence_of_letters_and_numbers)
    elif 'Slice' in command:
        start_index, end_index = int(command[1]), int(command[2])
        part_to_delete = sequence_of_letters_and_numbers[start_index:end_index]
        sequence_of_letters_and_numbers = sequence_of_letters_and_numbers.replace(part_to_delete, '')
        print(sequence_of_letters_and_numbers)

    command = input()

print(f"Your activation key is: {sequence_of_letters_and_numbers}")
