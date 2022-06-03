factor = int(input())
count = int(input())

lst = []

for number in range(factor, factor * count + 1):
    if number % factor == 0:
        lst.append(number)

print(lst)
