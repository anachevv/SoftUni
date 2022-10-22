def list_manipulator(lst, *args):
    commands = [x for x in args if isinstance(x, str)]
    numbers = args[2::]

    if commands[0] == 'add':
        if commands[1] == 'beginning':
            for i in range(len(numbers)):
                lst.insert(i, numbers[i])
        else:
            for i in numbers:
                lst.append(i)

        return lst

    elif commands[0] == 'remove':
        if commands[1] == 'beginning':
            if numbers:
                lst = lst[numbers[0]::]
            else:
                lst = lst[1::]
        else:
            if numbers:
                lst = lst[0:-numbers[0]]
            else:
                lst = lst[0:-1]

        return lst


print(list_manipulator([1,2,3], "remove", "end"))
print(list_manipulator([1,2,3], "remove", "beginning"))
print(list_manipulator([1,2,3], "add", "beginning", 20))
print(list_manipulator([1,2,3], "add", "end", 30))
print(list_manipulator([1,2,3], "remove", "end", 2))
print(list_manipulator([1,2,3], "remove", "beginning", 2))
print(list_manipulator([1,2,3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1,2,3], "add", "end", 30, 40, 50))
