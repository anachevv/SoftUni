n1 = int(input())
n2 = int(input())
operation = input()
result = 0

if operation == "+":
    result = n1 + n2
    if result % 2 == 0:
        even_or_odd = "even"
        print(f"{n1} {operation} {n2} = {result} - {even_or_odd}")
    else:
        even_or_odd = "odd"
        print(f"{n1} {operation} {n2} = {result} - {even_or_odd}")
elif operation == "-":
    result = n1 - n2
    if result % 2 == 0:
        even_or_odd = "even"
        print(f"{n1} {operation} {n2} = {result} - {even_or_odd}")
    else:
        even_or_odd = "odd"
        print(f"{n1} {operation} {n2} = {result} - {even_or_odd}")
elif operation == "*":
    result = n1 * n2
    if result % 2 == 0:
        even_or_odd = "even"
        print(f"{n1} {operation} {n2} = {result} - {even_or_odd}")
    else:
        even_or_odd = "odd"
        print(f"{n1} {operation} {n2} = {result} - {even_or_odd}")
elif operation == "/" and n1 != 0 and n2 != 0:
    result = n1 / n2
    print(f"{n1} {operation} {n2} = {result:.2f}")
elif operation == "%" and n1 != 0 and n2 != 0:
    result = n1 % n2
    print(f"{n1} {operation} {n2} = {result}")

if operation == "/" or operation == "%":
    if n1 == 0 or n2 == 0:
        print(f"Cannot divide {n1} by zero")
