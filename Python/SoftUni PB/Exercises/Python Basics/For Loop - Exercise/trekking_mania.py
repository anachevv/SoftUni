climber_groups = int(input())
number_count1 = 0
number_count2 = 0
number_count3 = 0
number_count4 = 0
number_count5 = 0

climbers = 0
total = 0
for x in range(climber_groups):
    climbers = int(input())
    total += climbers

    if climbers <= 5:
        number_count1 += climbers
    if 6 <= climbers <= 12:
        number_count2 += climbers
    if 13 <= climbers <= 25:
        number_count3 += climbers
    if 26 <= climbers <= 40:
        number_count4 += climbers
    if climbers >= 41:
        number_count5 += climbers

p1 = number_count1 / total * 100
p2 = number_count2 / total * 100
p3 = number_count3 / total * 100
p4 = number_count4 / total * 100
p5 = number_count5 / total * 100

print(f"{p1:.2f}%\n{p2:.2f}%\n{p3:.2f}%\n{p4:.2f}%\n{p5:.2f}%")
