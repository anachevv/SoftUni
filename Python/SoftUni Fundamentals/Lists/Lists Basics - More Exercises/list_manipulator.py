list_with_integers = input().split()
list_with_integers = [int(num) for num in list_with_integers]
command = input()


def exchange(list_int, index):
    if 0 <= index < len(list_int):
        return list_int[index + 1:] + list_int[:index + 1]
    else:
        return 'Invalid index'


def max_even(list_int):
    index = 0
    max_num = -2 ** 31
    is_found = False
    for i, num in enumerate(list_int):
        if num >= max_num and num % 2 == 0:
            max_num = num
            index = i
            is_found = True
    if is_found:
        return index
    else:
        return "No matches"


def max_odd(list_int):
    index = 0
    max_num = -2 ** 31
    is_found = False
    for i, num in enumerate(list_int):
        if num >= max_num and num % 2 != 0:
            max_num = num
            index = i
            is_found = True
    if is_found:
        return index
    else:
        return "No matches"


def min_even(list_int):
    index = 0
    min_num = 2 ** 31
    is_found = False
    for i, num in enumerate(list_int):
        if num <= min_num and num % 2 == 0:
            min_num = num
            index = i
            is_found = True
    if is_found:
        return index
    else:
        return "No matches"


def min_odd(list_int):
    index = 0
    min_num = 2 ** 31
    is_found = False
    for i, num in enumerate(list_int):
        if num <= min_num and num % 2 != 0:
            min_num = num
            index = i
            is_found = True
    if is_found:
        return index
    else:
        return "No matches"


def first_count_even(list_int, count_nums):
    result = []
    if count_nums > len(list_int):
        return "Invalid count"
    else:
        for num in list_int:
            if num % 2 == 0 and len(result) < count_nums:
                result.append(num)
        return result


def first_count_odd(list_int, count_nums):
    result = []
    if count_nums > len(list_int):
        return "Invalid count"
    else:
        for num in list_int:
            if num % 2 != 0 and len(result) < count_nums:
                result.append(num)
        return result


def last_count_even(list_int, count_nums):
    result = []
    if count_nums > len(list_int):
        return "Invalid count"
    else:
        for num in reversed(list_int):
            if num % 2 == 0 and len(result) < count_nums:
                result.insert(0, num)
        return result


def last_count_odd(list_int, count_nums):
    result = []
    if count_nums > len(list_int):
        return "Invalid count"
    else:
        for num in reversed(list_int):
            if num % 2 != 0 and len(result) < count_nums:
                result.insert(0, num)
        return result


while command != 'end':
    command = command.split()
    if 'exchange' in command:
        def_result = exchange(list_with_integers, int(command[1]))
        invalid = 'Invalid index'
        if def_result != invalid:
            list_with_integers = def_result
        else:
            print(invalid)
    elif 'max' in command:
        if 'even' in command:
            print(max_even(list_with_integers))
        else:
            print(max_odd(list_with_integers))
    elif 'min' in command:
        if 'even' in command:
            print(min_even(list_with_integers))
        else:
            print(min_odd(list_with_integers))
    elif 'first' in command:
        count = int(command[1])
        if 'even' in command:
            print(first_count_even(list_with_integers, count))
        else:
            print(first_count_odd(list_with_integers, count))
    elif 'last' in command:
        count = int(command[1])
        if 'even' in command:
            print(last_count_even(list_with_integers, count))
        else:
            print(last_count_odd(list_with_integers, count))

    command = input()

print(list_with_integers)
