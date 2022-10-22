sequence_of_items = input().split('|')
command = input()
stolen_items = []

while command != 'Yohoho!':
    if command == 'Yohoho!':
        break
    command = command.split()
    if 'Loot' in command:
        command.remove('Loot')
        for item in command:
            if item not in sequence_of_items:
                sequence_of_items.insert(0, item)

    elif 'Drop' in command:
        index = int(command[1])
        if 0 <= index < len(sequence_of_items):
            sequence_of_items.append(sequence_of_items[index])
            sequence_of_items.remove(sequence_of_items[index])

    elif 'Steal' in command:
        amount_of_items = int(command[1])
        if amount_of_items >= len(sequence_of_items):
            stolen_items = sequence_of_items
            print(', '.join(stolen_items))
            print('Failed treasure hunt.')
            exit()
        else:
            stolen_items = sequence_of_items[-amount_of_items:]
            del sequence_of_items[-amount_of_items:]
            print(', '.join(stolen_items))

    command = input()

if sequence_of_items:
    average_sum = sum(len(item) for item in sequence_of_items) / len(sequence_of_items)
    print(f'Average treasure gain: {average_sum:.2f} pirate credits.')
else:
    print("Failed treasure hunt.")
