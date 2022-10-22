matrix = []
rows = int(input())
columns = rows
for row in range(rows):
    lst = [int(x) for x in input().split(', ')]
    matrix.append(lst)

primary_diagonal = [matrix[i][i] for i in range(len(matrix))]
secondary_diagonal = [matrix[i][len(matrix) - 1 - i] for i in range(len(matrix))]
print(f"Primary diagonal: {', '.join(str(x) for x in primary_diagonal)}. Sum: {sum(primary_diagonal)}")
print(f"Secondary diagonal: {', '.join(str(x) for x in secondary_diagonal)}. Sum: {sum(secondary_diagonal)}")
