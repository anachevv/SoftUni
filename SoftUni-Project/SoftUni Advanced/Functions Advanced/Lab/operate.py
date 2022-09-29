def operate(operator, *args):
    def add(*args):
        return sum(args)

    def substract(result, *args):
        return result + sum(-num for num in args)

    def multiply(*args):
        result = 1
        for i in args:
            result *= i
        return result

    def divide(x, *args):
        result = x
        for i in args:
            result /= i
        return result

    if operator == '+':
        return add(*args)
    elif operator == '-':
        return substract(*args)
    elif operator == '*':
        return multiply(*args)
    elif operator == '/':
        return divide(*args)

print(operate("+", 1, 2, 3))
print(operate("-", 1, 2, 3))
print(operate("*", 3, 4))
print(operate("/", 3, 4, 2, 3))
