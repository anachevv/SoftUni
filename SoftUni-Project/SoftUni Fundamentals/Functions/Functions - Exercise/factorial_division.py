def factorial_division(first, second):
    first_sum = 1
    for curr in range(1, first + 1):
        first_sum *= curr

    second_sum = 1
    for curr in range(1, second + 1):
        second_sum *= curr

    return f"{(first_sum / second_sum):.2f}"


first_number = int(input())
second_number = int(input())

print(factorial_division(first_number, second_number))
