numbers = [float(num) for num in input().split()]
dct = {}
for number in numbers:
    if number not in dct:
        dct[number] = 0
    dct[number] += 1

for number, count in dct.items():
    print(f"{number} - {count} times")
