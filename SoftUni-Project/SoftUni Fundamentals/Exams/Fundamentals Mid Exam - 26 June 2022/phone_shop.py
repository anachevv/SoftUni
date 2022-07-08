sequence_of_phones = input().split(', ')
command = input()

while command != 'End':
    if command == 'End':
        break
    command = command.split(' - ')

    if 'Add' in command:
        phone = command[1]
        if phone not in sequence_of_phones:
            sequence_of_phones.append(phone)
    elif 'Remove' in command:
        phone = command[1]
        if phone in sequence_of_phones:
            sequence_of_phones.remove(phone)
    elif 'Bonus phone' in command:
        phones = command[1].split(':')
        old_phone = phones[0]
        new_phone = phones[1]
        if old_phone in sequence_of_phones:
            old_phone_index = sequence_of_phones.index(old_phone)
            sequence_of_phones.insert(old_phone_index + 1, new_phone)
    elif 'Last' in command:
        phone = command[1]
        if phone in sequence_of_phones:
            sequence_of_phones.remove(phone)
            sequence_of_phones.append(phone)

    command = input()

print(", ".join(sequence_of_phones))
