import sys

n = int(input())
min_number = 100000000000000000000000
number = 0

for x in range(n):
    number = int(input())

    if number < min_number:
        min_number = number

print(min_number)
