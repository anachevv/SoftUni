def move(direction, row, col):
    if direction == 'up':
        return row - 1, col
    if direction == 'down':
        return row + 1, col
    if direction == 'left':
        return row, col - 1
    if direction == 'right':
        return row, col + 1


def invalid_move(row, col, size):
    return row < 0 or row >= size or col < 0 or col >= size


size = int(input())
matrix = []
food = 0
snake_pos = []
burrow_pos = []

for row in range(size):
    lst = [x for x in input()]

    if 'S' in lst:
        snake_pos = [row, lst.index('S')]
    if 'B' in lst:
        burrow_pos.append([row, lst.index('B')])

    matrix.append(lst)


while True:
    command = input()
    next_row, next_col = move(command, snake_pos[0], snake_pos[1])

    if invalid_move(next_row, next_col, size):
        matrix[snake_pos[0]][snake_pos[1]] = '.'
        break

    matrix[snake_pos[0]][snake_pos[1]] = '.'

    if matrix[next_row][next_col] == '*':
        snake_pos[0], snake_pos[1] = next_row, next_col
        food += 1
        matrix[next_row][next_col] = 'S'

    elif matrix[next_row][next_col] == 'B':
        matrix[next_row][next_col] = '.'
        snake_pos = [burrow_pos[1][0], burrow_pos[1][1]]
        matrix[snake_pos[0]][snake_pos[1]] = 'S'
        continue

    snake_pos = [next_row, next_col]

    if food == 10:
        break


if food == 10:
    print("You won! You fed the snake.")
else:
    print("Game over!")

print(f"Food eaten: {food}")

for row in matrix:
    print(''.join(x for x in row))
