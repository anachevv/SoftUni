number_of_wagons = int(input())
train_list = [0] * number_of_wagons

command = input().split()
while command != ['End']:
    if command == ['End']:
        break
    if command[0] == 'add':
        people_to_add = int(command[1])
        train_list[-1] += people_to_add
    elif command[0] == 'insert':
        wagon_index = int(command[1])
        people_to_insert = int(command[2])
        train_list[wagon_index] += people_to_insert
    elif command[0] == 'leave':
        index = int(command[1])
        people_to_leave = int(command[2])
        train_list[index] -= people_to_leave

    command = input().split()

print(train_list)
