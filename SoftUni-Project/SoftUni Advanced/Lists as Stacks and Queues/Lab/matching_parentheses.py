string = input()
lst = []
for index in range(len(string)):
    if string[index] == '(':
        lst.append(index)
    elif string[index] == ')':
        start_index = lst.pop()
        print(string[start_index: index + 1])
