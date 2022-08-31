numbers = [int(num) for num in input().split()]
stack = []
while numbers:
    stack.append(numbers.pop())

reversed_string = " ".join(str(num) for num in stack)
print(reversed_string)
