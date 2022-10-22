def calculations(operation=input(), first_number=int(input()), second_number=int(input())):

    result = 0

    if operation == 'multiply':
        result = first_number * second_number
    elif operation == 'divide':
        result = first_number / second_number
    elif operation == 'add':
        result = first_number + second_number
    elif operation == 'subtract':
        result = first_number - second_number

    return int(result)


print(calculations())
