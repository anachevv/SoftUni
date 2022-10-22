rows, columns = [int(x) for x in input().split()]
matrix = []
for row in range(rows):
    lst = [char for char in input().split()]
    matrix.append(lst)

identical_chars_squares = 0
for row in range(rows - 1):
    for column in range(columns - 1):
        lst = [matrix[row][column], matrix[row][column + 1], matrix[row + 1][column], matrix[row + 1][column + 1]]
        if lst[0] == lst[1] == lst[2] == lst[3]:
            identical_chars_squares += 1
print(identical_chars_squares)
