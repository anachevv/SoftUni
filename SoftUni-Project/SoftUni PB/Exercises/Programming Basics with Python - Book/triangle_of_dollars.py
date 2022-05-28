n = int(input())

for row in range(n):
    print("$", end="")
    for column in range(row):
        print(" $", end="")
    print()
