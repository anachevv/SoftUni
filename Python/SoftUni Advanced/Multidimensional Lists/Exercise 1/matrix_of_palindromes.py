from string import ascii_lowercase

rows, columns = [int(x) for x in input().split()]
alpha_lower = [letter for letter in ascii_lowercase]
alpha_pos = {index: letter for (index, letter) in enumerate(alpha_lower)}

result = []
for row in range(rows):
    lst = []
    for column in range(columns):
        middle = alpha_pos[row + column]
        string = alpha_pos[row] + middle + alpha_pos[row]
        if string == string[::-1]:
            lst.append(string)
    result.append(lst)

for row in result:
    print(' '.join(x for x in row))
