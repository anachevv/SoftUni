rows = int(input())
columns = rows
matrix = []

'''
[[11, 2, 4], [4, 5, 6], [10, 8, -12]]
'''

for r in range(rows):
    row = [int(x) for x in input().split()]
    matrix.append(row)

diagonal_numbers = []
i = 0
for row_index in range(rows):
    for column_index in range(columns):
        if i == columns:
            break
        diagonal_numbers.append(matrix[column_index][i])
        i += 1
diagonal_sum = sum(diagonal_numbers)
print(diagonal_sum)
