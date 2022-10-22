command = input()

while command != 'End':
    new_word = ''.join(char * 2 for char in command)

    if command != 'SoftUni':
        print(new_word)

    command = input()
