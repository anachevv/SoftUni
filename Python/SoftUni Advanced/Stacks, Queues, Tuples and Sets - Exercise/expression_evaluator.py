from math import floor


def get_expr(expr):
    for index in range(len(expr)):
        if expr[index].isdigit() or len(expr[index]) > 1:
            expr[index] = int(expr[index])
    return expr


def evaluator(expr):
    expr = get_expr(expr)
    numbers = []
    result = int(expr.pop(0))
    for element in expr:
        if element not in ('*', '/', '+', '-'):
            numbers.append(element)
        else:
            if element == '-':
                for num in numbers:
                    result -= num
            elif element == '+':
                for num in numbers:
                    result += num
            elif element == '*':
                for num in numbers:
                    result *= num
            elif element == '/':
                for num in numbers:
                    result /= num
                    result = floor(result)
            numbers = []
    return result


expr = [x for x in input().split()]
print(evaluator(expr))
