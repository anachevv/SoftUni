rows = int(input())
matrix = []

for row in range(rows):
    lst = [int(x) for x in input().split()]
    matrix.append(lst)

command = input()
while command != 'END':
    command = command.split()
    row, col, value = [int(x) for x in command[1::]]
    
    if 0 > row or row > rows - 1 or 0 > col or col > rows - 1:
        print("Invalid coordinates")
    else:
        if command[0] == 'Add':
            matrix[row][col] += value
        else:
            matrix[row][col] -= value

    command = input()

for lst in matrix:
    print(" ".join(str(x) for x in lst))
