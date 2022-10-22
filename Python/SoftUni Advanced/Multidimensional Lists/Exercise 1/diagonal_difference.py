matrix = []
rows = int(input())
columns = rows
for row in range(rows):
    lst = [int(x) for x in input().split()]
    matrix.append(lst)

primary_diagonal_sum = sum([matrix[i][i] for i in range(len(matrix))])
secondary_diagonal_sum = sum([matrix[i][len(matrix) - 1 - i] for i in range(len(matrix))])
difference = abs(primary_diagonal_sum - secondary_diagonal_sum)
print(difference)
