size = int(input())
matrix = []
bunny_pos = []
max_eggs = 0
best_direction = ""
best_path = []

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

for row in range(size):
    lst = input().split()
    if 'B' in lst:
        bunny_pos = [row, lst.index('B')]

    matrix.append(lst)

for direction, position in directions.items():
    path = []
    eggs = 0
    row, column = [bunny_pos[0] + position[0], bunny_pos[1] + position[1]]

    while 0 <= row < size and 0 <= column < size:
        if matrix[row][column] == 'X':
            break
        eggs += int(matrix[row][column])
        path.append([row, column])

        row += position[0]
        column += position[1]

    if eggs >= max_eggs:
        max_eggs = eggs
        best_direction = direction
        best_path = path

print(best_direction)
print(*best_path, sep='\n')
print(max_eggs)
