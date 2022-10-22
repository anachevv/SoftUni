rows, columns = [int(x) for x in input().split()]
matrix = []
for row in range(rows):
    matrix.append(input().split())

is_valid = True
command = input()
while command != 'END':
    command = command.split()
    if command[0] == 'swap' and len(command) == 5:
        command = command[1::]
        command = [int(x) for x in command]
        first_row, first_column, second_row, second_column = command
        for index in command:
            if index < 0:
                is_valid = False
                break
        if not is_valid:
            print('Invalid input!')
            continue
        if first_row < rows and second_row < rows and first_column < columns and second_column < columns:
            is_valid = True
            matrix[first_row][first_column], matrix[second_row][second_column] = matrix[second_row][second_column], matrix[first_row][first_column]
            for lst in matrix:
                print(' '.join(x for x in lst))
        else:
            print('Invalid input!')
    else:
        print('Invalid input!')
    command = input()
