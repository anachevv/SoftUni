def snake(rows, columns, word):
    index = 0
    result = ""

    for row in range(rows):
        elements = [''] * columns
        if row % 2 == 0:
            for column in range(columns):
                elements[column] = word[index % len(word)]
                index += 1
        else:
            for column in range(columns - 1, -1, -1):
                elements[column] = word[index % len(word)]
                index += 1
        result += "".join(elements) + '\n'

    return result


rows, columns = [int(x) for x in input().split()]
word = input()

print(snake(rows, columns, word))
