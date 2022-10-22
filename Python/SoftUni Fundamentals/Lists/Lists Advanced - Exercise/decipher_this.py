list_of_words = [x for x in input().split()]

'''
['72olle', '103doo', '100ya']
'''

for string in list_of_words:
    secret_letter = ''
    for char in string:
        if char.isdigit():
            secret_letter += char
    string = string.replace(secret_letter, chr(int(secret_letter)))
    current_list = [x for x in string]
    current_list[1], current_list[-1] = current_list[-1], current_list[1]

    print(''.join(current_list), end=' ')
