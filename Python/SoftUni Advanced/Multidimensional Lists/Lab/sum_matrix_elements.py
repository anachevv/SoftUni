rows, columns = [int(num) for num in input().split(', ')]
matrix = []
total_sum = 0
for i in range(rows):
    row = [int(x) for x in input().split(', ')]
    total_sum += sum(row)
    matrix.append(row)
print(total_sum)
print(matrix)
