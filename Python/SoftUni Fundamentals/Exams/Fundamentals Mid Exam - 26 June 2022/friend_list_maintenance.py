sequence_of_friends = input().split(', ')
command = input()
blacklisted_names = 0
lost_names = 0
list_of_lost_names = []

while command != 'Report':
    if command == 'Report':
        break
    command = command.split()

    if 'Blacklist' in command:
        name = command[1]
        if name in sequence_of_friends:
            name_index = sequence_of_friends.index(name)
            sequence_of_friends[name_index] = 'Blacklisted'
            blacklisted_names += 1
            print(f"{name} was blacklisted.")
        else:
            print(f"{name} was not found.")
    elif 'Error' in command:
        index = int(command[1])
        if 0 <= index < len(sequence_of_friends):
            if sequence_of_friends[index] != 'Blacklisted' and sequence_of_friends[index] in sequence_of_friends:
                if sequence_of_friends[index] not in list_of_lost_names:
                    name = sequence_of_friends[index]
                    sequence_of_friends[index] = 'Lost'
                    if name != 'Lost':
                        lost_names += 1
                        print(f"{name} was lost due to an error.")
    elif 'Change' in command:
        if 0 <= int(command[1]) < len(sequence_of_friends):
            index = int(command[1])
            current_name = sequence_of_friends[index]
            tmp = current_name
            next_new_name = command[2]
            sequence_of_friends[index] = next_new_name
            print(f"{tmp} changed his username to {next_new_name}.")

    command = input()

print(f"Blacklisted names: {blacklisted_names}")
print(f"Lost names: {lost_names}")
print(" ".join(sequence_of_friends))
