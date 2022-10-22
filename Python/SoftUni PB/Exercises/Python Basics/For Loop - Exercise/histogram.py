n = int(input())
number_count1 = 0
number_count2 = 0
number_count3 = 0
number_count4 = 0
number_count5 = 0

for x in range(n):
    number = int(input())

    if number < 200:
        number_count1 += 1
    if 200 <= number <= 399:
        number_count2 += 1
    if 400 <= number <= 599:
        number_count3 += 1
    if 600 <= number <= 799:
        number_count4 += 1
    if number >= 800:
        number_count5 += 1

p1 = number_count1 / n * 100
p2 = number_count2 / n * 100
p3 = number_count3 / n * 100
p4 = number_count4 / n * 100
p5 = number_count5 / n * 100

print(f"{p1:.2f}%\n{p2:.2f}%\n{p3:.2f}%\n{p4:.2f}%\n{p5:.2f}%")
