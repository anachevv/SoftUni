user_input = input()

receiving_list = [x for x in user_input.split(' ')]

lst = [int(('-' + i)) if int(i) > 0 else int(i.replace('-', '')) for i in receiving_list]

print(lst)
