divisor = int(input())
boundary = int(input())

number = 0
special_number = 0

for number in range(1, boundary + 1):
    if 0 < number <= boundary and number % divisor == 0:
        special_number = number
    if number > special_number:
        number = special_number

print(number)
