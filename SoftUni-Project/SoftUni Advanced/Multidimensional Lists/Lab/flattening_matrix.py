rows = int(input())
matrix = []
for r in range(rows):
    numbers = [int(x) for x in input().split(', ')]
    for number in numbers:
        matrix.append(number)
print(matrix)
