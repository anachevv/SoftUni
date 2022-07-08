def data_types(type_of_string, second):

    if type_of_string == 'int':
        second = int(second) * 2
    elif type_of_string == 'real':
        second = f"{(float(second) * 1.5):.2f}"
    elif type_of_string == 'string':
        second = '$' + second + '$'

    return second


first_string = input()
second_string = input()

print(data_types(first_string, second_string))
