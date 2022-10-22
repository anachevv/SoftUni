sequence_of_items = input().split(', ')
command = input()

while command != 'Craft!':
    if command == 'Craft':
        break
    command = command.split(' - ')

    if 'Collect' in command:
        item = command[1]
        if item not in sequence_of_items:
            sequence_of_items.append(item)
    elif 'Drop' in command:
        item = command[1]
        if item in sequence_of_items:
            sequence_of_items.remove(item)
    elif 'Combine Items' in command:
        items = command[1].split(':')
        old_item = items[0]
        new_item = items[1]
        if old_item in sequence_of_items:
            sequence_of_items.insert(sequence_of_items.index(old_item) + 1, new_item)
    elif 'Renew' in command:
        item = command[1]
        if item in sequence_of_items:
            sequence_of_items.remove(item)
            sequence_of_items.append(item)

    command = input()

print(', '.join(sequence_of_items))
