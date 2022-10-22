sequence_of_groceries = input().split('!')
command = input()

while command != "Go Shopping!":
    if command == 'Go Shopping!':
        break
    command = command.split()
    if 'Urgent' in command:
        item = command[1]
        if item not in sequence_of_groceries:
            sequence_of_groceries.insert(0, item)
    elif 'Unnecessary' in command:
        item = command[1]
        if item in sequence_of_groceries:
            sequence_of_groceries.remove(item)
    elif 'Correct' in command:
        old_item = command[1]
        new_item = command[2]
        if old_item in sequence_of_groceries:
            old_item_index = sequence_of_groceries.index(old_item)
            sequence_of_groceries.remove(old_item)
            sequence_of_groceries.insert(old_item_index, new_item)
    elif 'Rearrange' in command:
        grocery = command[1]
        if grocery in sequence_of_groceries:
            sequence_of_groceries.remove(grocery)
            sequence_of_groceries.append(grocery)

    command = input()

print(', '.join(sequence_of_groceries))
