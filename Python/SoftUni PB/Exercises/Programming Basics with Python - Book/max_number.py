n = int(input())
max_number = -100000000000000000000

for x in range(n):
    number = int(input())

    if number > max_number:
        max_number = number

print(max_number)
