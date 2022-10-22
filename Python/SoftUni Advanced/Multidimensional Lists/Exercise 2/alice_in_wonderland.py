size = int(input())
tea_bags = 0
matrix = []
alice_position = []

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

for row in range(size):
    lst = input().split()
    if 'A' in lst:
        alice_position += [row, lst.index('A')]
        lst[alice_position[1]] = '*'

    matrix.append(lst)

while True:
    command = input()

    if command in directions:
        row, column = [alice_position[0] + directions[command][0], alice_position[1] + directions[command][1]]

        if 0 > row or row >= size or 0 > column or column >= size:
            print("Alice didn't make it to the tea party.")
            break

        elif matrix[row][column] == 'R':
            matrix[row][column] = '*'
            print("Alice didn't make it to the tea party.")
            break

        alice_position = [row, column]

        if matrix[row][column] not in ('.', '*'):
            tea_bags += int(matrix[row][column])

        matrix[row][column] = '*'

        if tea_bags >= 10:
            print("She did it! She went to the party.")
            break

for row in matrix:
    print(' '.join(row))
