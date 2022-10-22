command = input()

while command != 'end':
    string = command
    reversed_string = "".join(string[::-1])
    print(f"{command} = {reversed_string}")

    command = input()

