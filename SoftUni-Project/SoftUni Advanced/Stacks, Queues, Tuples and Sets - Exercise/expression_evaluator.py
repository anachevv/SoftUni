from math import floor

'''
['1', '0', '2', '3', '*', '4', '2', '/', '3', '0', '1', '0', '+', '1', '0', '0', '5', '0', '-', '2', '-', '1', '*']
'''
def get_expr(expr):
    for index in range(len(expr)):
        if expr[index].isdigit() or len(expr[index]) > 1:
            expr[index] = int(expr[index])
    return expr

def evaluator(expr):
    numbers = []
    result = int(expr.pop(0))
    for element in expr:
        if element.isnumeric():
            numbers.append(int(element))
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
# ALMOST DONE!