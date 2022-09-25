rows, columns = [int(x) for x in input().split()]
matrix = []
for row in range(rows):
    lst = [int(x) for x in input().split()]
    matrix.append(lst)
'''
[   
    [1, 5, 5, 2, 4],
    [2, 1, 4, 14, 3],
    [3, 7, 11, 2, 8], 
    [4, 8, 12, 16, 4]
]
'''
max_sum = -100000
result = []
for row in range(rows - 2):
    triple_pair = []
    for column in range(columns - 2):
        triple_pair = [matrix[row][column], matrix[row][column + 1], matrix[row][column + 2],
                       matrix[row + 1][column], matrix[row + 1][column + 1], matrix[row + 1][column + 2],
                       matrix[row + 2][column], matrix[row + 2][column + 1], matrix[row + 2][column + 2]]
        pair_sum = sum(triple_pair)
        if pair_sum > max_sum:
            max_sum = pair_sum
            result = triple_pair

print(f"Sum = {max_sum}")
print(result[0], result[1], result[2])
print(result[3], result[4], result[5])
print(result[6], result[7], result[8])
