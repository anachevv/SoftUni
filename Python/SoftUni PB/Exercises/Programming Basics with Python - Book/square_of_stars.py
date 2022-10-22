n = int(input())

for row in range(1, n + 1):
    print("*", end="")
    for column in range(1, n):
        print(" *", end="")
    print()
