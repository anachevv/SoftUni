rows, columns = [int(x) for x in input().split(', ')]
matrix = []
for r in range(rows):
    row = [int(num) for num in input().split()]
    matrix.append(row)

columns_sums = [0] * columns
for row_index in range(rows):
    for column_index in range(columns):
        columns_sums[column_index] += matrix[row_index][column_index]
print("\n".join(str(num) for num in columns_sums))
