import string


def get_number(strings):
    numbers = []
    for element in strings:
        number = ""
        for char in element:
            if char.isnumeric():
                number += char
        numbers.append(int(number))
    return numbers


def calculate_result(strings):
    list_with_numbers = get_number(strings)

    result = 0
    for index, number in enumerate(list_with_numbers):
        if strings[index][0].isupper():
            alpha_position = string.ascii_uppercase.index(strings[index][0]) + 1
            number /= alpha_position
        elif strings[index][0].islower():
            alpha_position = string.ascii_lowercase.index(strings[index][0]) + 1
            number *= alpha_position

        if strings[index][-1].isupper():
            alpha_position = string.ascii_uppercase.index(strings[index][-1]) + 1
            number -= alpha_position
        else:
            alpha_position = string.ascii_lowercase.index(strings[index][-1]) + 1
            number += alpha_position

        result += number
    return f'{result:.2f}'


sequence_of_strings = input().split()
print(calculate_result(sequence_of_strings))
