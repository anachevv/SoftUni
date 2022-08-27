command = input()
lst = []
while command != 'End':
    if command == 'Paid':
        print("\n".join(lst))
        lst.clear()
    else:
        lst.append(command)

    command = input()
print("{} people remaining.".format(len(lst)))
