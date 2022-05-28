n_times = int(input())

for string in range(n_times):
    current_string = input()
    forbidden_chars = [',', '.', '_']
    pure = True
    for character in current_string:
        if character in forbidden_chars:
            pure = False
    if pure is True:
        print(f'{current_string} is pure.')
    else:
        print(f'{current_string} is not pure!')
