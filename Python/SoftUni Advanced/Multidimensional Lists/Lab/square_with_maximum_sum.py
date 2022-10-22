rows, columns = [int(num) for num in input().split(', ')]
matrix = []
for r in range(rows):
    row = [int(x) for x in input().split(', ')]
    matrix.append(row)

lst = []
max_sum = -100000
for row in range(rows - 1):
    double_pair = []
    for column in range(columns - 1):
        double_pair = [matrix[row][column], matrix[row][column + 1], matrix[row + 1][column], matrix[row + 1][column + 1]]
        pair_sum = sum(double_pair)
        if pair_sum > max_sum:
            max_sum = pair_sum
            lst = double_pair

print(lst[0], lst[1])
print(lst[2], lst[3])
print(max_sum)
