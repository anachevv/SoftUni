def do_math(expr):
    first_number, operation, second_number = float(expr.split()[0]), expr.split()[1], int(expr.split()[2])
    result = 0
    if operation == '*':
        result = first_number * second_number
    elif operation == '/':
        result = first_number / second_number
    elif operation == '-':
        result = first_number - second_number
    elif operation == '+':
        result = first_number + second_number
    elif operation == '^':
        result = first_number ** second_number
    return f"{result:.2f}"
