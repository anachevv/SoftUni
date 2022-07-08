lst = []

command = input()
while command != 'End':
    if command == 'End':
        break
    note = command.split('-')
    priority = int(note[0])

    if priority != 0:
        note[0] = priority
        lst.append(note)
    command = input()


sorted_list = [element[1] for element in sorted(lst)]

print(sorted_list)
