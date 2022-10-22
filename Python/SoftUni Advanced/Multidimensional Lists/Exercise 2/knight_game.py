def move(matrix, row, column):
    moves = [
        [row - 2, column - 1],
        [row - 2, column + 1],
        [row - 1, column - 2],
        [row - 1, column + 2],
        [row + 1, column - 2],
        [row + 1, column + 2],
        [row + 2, column - 1],
        [row + 2, column + 1]
    ]

    knights = 0

    for r, c in moves:
        if 0 <= r < len(matrix) and 0 <= c < len(matrix) and matrix[r][c] == 'K':
            knights += 1

    return knights


size = int(input())
matrix = [list(input()) for x in range(size)]
knights_to_remove = 0

while True:
    max_attacks = 0
    best_knight = []

    for row in range(size):
        for column in range(size):
            if matrix[row][column] == 'K':
                attacks = move(matrix, row, column)

                if attacks > max_attacks:
                    max_attacks = attacks
                    best_knight = [row, column]

    if best_knight:
        matrix[best_knight[0]][best_knight[1]] = '0'
        knights_to_remove += 1
    else:
        break

print(knights_to_remove)
