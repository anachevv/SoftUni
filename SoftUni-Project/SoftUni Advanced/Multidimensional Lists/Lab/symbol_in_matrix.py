rows = int(input())
columns = rows
matrix = []
for r in range(rows):
    row = input()
    matrix.append([char for char in row])

symbol = input()
symbol_coordinates = []
symbol_is_found = False
for row in range(rows):
    for column in range(columns):
        if matrix[row][column] == symbol:
            symbol_coordinates.append(row)
            symbol_coordinates.append(column)
            symbol_is_found = True
            break
    if symbol_is_found:
        break
if symbol_is_found:
    print(f"({', '.join(str(x) for x in symbol_coordinates)})")
else:
    print(f"{symbol} does not occur in the matrix")
