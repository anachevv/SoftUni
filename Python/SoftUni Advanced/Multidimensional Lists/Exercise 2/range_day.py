size = 5
matrix = []
my_pos = []
total_targets = 0


def move(direction, row, col, steps):
    if direction == 'up':
        return row - steps, col
    if direction == 'down':
        return row + steps, col
    if direction == 'left':
        return row, col - steps
    if direction == 'right':
        return row, col + steps


def is_outside(row, col, size):
    return row < 0 or col < 0 or row >= size or col >= size


for row in range(size):
    row_elements = input().split()
    matrix.append(row_elements)

    for col in range(size):
        if row_elements[col] == 'x':
            total_targets += 1
        elif row_elements[col] == 'A':
            my_pos = [row, col]

targets_left = total_targets
hit_targets = []

number_of_commands = int(input())

for _ in range(number_of_commands):
    command_args = input().split()
    command = command_args[0]
    direction = command_args[1]

    if command == 'move':
        steps = int(command_args[2])
        next_row, next_col = move(direction, my_pos[0], my_pos[1], steps)

        if is_outside(next_row, next_col, size) or matrix[next_row][next_col] != '.':
            continue

        matrix[my_pos[0]][my_pos[1]] = '.'
        my_pos[0], my_pos[1] = next_row, next_col
        matrix[my_pos[0]][my_pos[1]] = 'A'

    elif command == 'shoot':
        shoot_row, shoot_col = my_pos[0], my_pos[1]
        while True:
            shoot_row, shoot_col = move(direction, shoot_row, shoot_col, 1)

            if is_outside(shoot_row, shoot_col, size):
                break

            if matrix[shoot_row][shoot_col] == 'x':
                targets_left -= 1
                matrix[shoot_row][shoot_col] = '.'
                hit_targets.append([shoot_row, shoot_col])
                break

        if targets_left == 0:
            break

if targets_left == 0:
    print(f'Training completed! All {total_targets} targets hit.')
else:
    print(f'Training not completed! {targets_left} targets left.')

print(*hit_targets, sep='\n')
