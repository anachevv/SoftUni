def move(direction, row, col):
    if direction == 'up':
        return row - 1, col
    if direction == 'down':
        return row + 1, col
    if direction == 'left':
        return row, col - 1
    if direction == 'right':
        return row, col + 1


size = int(input())
racing_number = input()
car_pos = [0, 0]
matrix = []
tunnels_pos = []
total_distance = 0
is_disqualified = True

for row in range(size):
    lst = input().split()
    if 'T' in lst:
        tunnels_pos.append([row, lst.index('T')])

    matrix.append(lst)


while True:
    command = input()

    if command == 'End':
        matrix[car_pos[0]][car_pos[1]] = 'C'
        break

    next_row, next_col = move(command, car_pos[0], car_pos[1])

    matrix[car_pos[0]][car_pos[1]] = '.'

    if matrix[next_row][next_col] == 'T':
        matrix[next_row][next_col] = '.'
        car_pos = [tunnels_pos[1][0], tunnels_pos[1][1]]
        matrix[car_pos[0]][car_pos[1]] = 'C'
        total_distance += 30
        continue

    car_pos = [next_row, next_col]
    total_distance += 10

    if matrix[next_row][next_col] == 'F':
        # car_pos = [next_row, next_col]s
        matrix[car_pos[0]][car_pos[1]] = 'C'
        # total_distance += 10
        is_disqualified = False
        break


if not is_disqualified:
    print(f"Racing car {racing_number} finished the stage!")
else:
    print(f"Racing car {racing_number} DNF.")

print(f"Distance covered {total_distance} km.")

for row in matrix:
    print(''.join(row))
