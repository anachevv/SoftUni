def sum_numbers(first, second):
    return first + second


def subtract(sum, third):
    return sum - third


def add_and_subtract(first, second, third):
    total_sum = sum_numbers(first, second)
    result = subtract(total_sum, third)

    return result


first_number = int(input())
second_number = int(input())
third_number = int(input())

print(add_and_subtract(first_number, second_number, third_number))
