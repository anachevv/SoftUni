n = int(input())
result = 0
p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0
p6 = 0

for x in range(n):
    number = int(input())

    if 0 <= number <= 9:
        result += 0.2 * number
        p1 += 1
    elif 10 <= number <= 19:
        result += 0.3 * number
        p2 += 1
    elif 20 <= number <= 29:
        result += 0.4 * number
        p3 += 1
    elif 30 <= number <= 39:
        result += 50
        p4 += 1
    elif 40 <= number <= 50:
        result += 100
        p5 += 1
    elif number < 0 or number > 50:
        result /= 2
        p6 += 1

print(f"{result:.2f}")
print(f"From 0 to 9: {p1 / (p1 + p2 + p3 + p4 + p5 + p6) * 100:.2f}%")
print(f"From 10 to 19: {p2/ (p1 + p2 + p3 + p4 + p5 + p6) * 100:.2f}%")
print(f"From 20 to 29: {p3 / (p1 + p2 + p3 + p4 + p5 + p6) * 100:.2f}%")
print(f"From 30 to 39: {p4 / (p1 + p2 + p3 + p4 + p5 + p6) * 100:.2f}%")
print(f"From 40 to 50: {p5 / (p1 + p2 + p3 + p4 + p5 + p6) * 100:.2f}%")
print(f"Invalid numbers: {p6 / (p1 + p2 + p3 + p4 + p5 + p6) * 100:.2f}%")
