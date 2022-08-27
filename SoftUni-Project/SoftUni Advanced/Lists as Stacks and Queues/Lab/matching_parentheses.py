string = input()
results = []
for index in range(len(string)):
    if string[index] == '(':
        results.append(index)
    elif string[index] == ')':
        start_index = results.pop()
        print(string[start_index: index + 1])
