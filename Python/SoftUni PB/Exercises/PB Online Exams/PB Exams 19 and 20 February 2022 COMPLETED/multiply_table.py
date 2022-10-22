number = int(input())

reversed_number = 0

while number > 0:
    remainder = number % 10
    reversed_number = (reversed_number * 10) + remainder
    number = number // 10

str_reversed_number = str(reversed_number)

for first_digit in range(1, int(str_reversed_number[0]) + 1):
    for second_digit in range(1, int(str_reversed_number[1]) + 1):
        for third_digit in range(1, int(str_reversed_number[2]) + 1):
            result = first_digit * second_digit * third_digit
            print(f"{first_digit} * {second_digit} * {third_digit} = {result}")
