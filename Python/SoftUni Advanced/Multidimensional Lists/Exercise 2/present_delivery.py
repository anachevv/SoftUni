def move(direction, row, col):
    directions = {
        'up': (-1, 0),
        'down': (1, 0),
        'left': (0, -1),
        'right': (0, 1)
    }

    nex_row, next_col = [row + directions[direction][0], col + directions[direction][1]]

    return [nex_row, next_col]


presents = int(input())
size = int(input())

matrix = []
santa_row = 0
santa_col = 0
nice_kids = 0
received_presents = 0

for row in range(size):
    lst = input().split()

    if 'S' in lst:
        santa_row, santa_col = [row, lst.index('S')]
    if 'V' in lst:
        nice_kids += lst.count('V')

    matrix.append(lst)


while True:
    command = input()
    if command == 'Christmas morning':
        break

    matrix[santa_row][santa_col] = '-'

    santa_row, santa_col = move(command, santa_row, santa_col)

    if matrix[santa_row][santa_col] == 'V':
        presents -= 1
        received_presents += 1

    elif matrix[santa_row][santa_col] == 'C':
        if matrix[santa_row][santa_col - 1] == 'V' and presents:
            received_presents += 1
            presents -= 1
            matrix[santa_row][santa_col - 1] = '-'
        elif matrix[santa_row][santa_col - 1] == 'X' and presents:
            presents -= 1
            matrix[santa_row][santa_col - 1] = '-'

        if matrix[santa_row][santa_col + 1] == 'V' and presents:
            received_presents += 1
            presents -= 1
            matrix[santa_row][santa_col + 1] = '-'
        elif matrix[santa_row][santa_col + 1] == 'X' and presents:
            presents -= 1
            matrix[santa_row][santa_col + 1] = '-'

        if matrix[santa_row - 1][santa_col] == 'V' and presents:
            received_presents += 1
            presents -= 1
            matrix[santa_row - 1][santa_col] = '-'
        elif matrix[santa_row - 1][santa_col] == 'X' and presents:
            presents -= 1
            matrix[santa_row - 1][santa_col] = '-'

        if matrix[santa_row + 1][santa_col] == 'V' and presents:
            received_presents += 1
            presents -= 1
            matrix[santa_row + 1][santa_col] = '-'
        elif matrix[santa_row + 1][santa_col] == 'X' and presents:
            presents -= 1
            matrix[santa_row + 1][santa_col] = '-'

    matrix[santa_row][santa_col] = 'S'

    if presents == 0 or received_presents == nice_kids:
        break


if presents == 0 and received_presents < nice_kids:
    print('Santa ran out of presents!')

for row in matrix:
    print(*row, sep=' ')

if received_presents == nice_kids:
    print(f"Good job, Santa! {nice_kids} happy nice kid/s.")
else:
    print(f'No presents for {nice_kids - received_presents} nice kid/s.')
