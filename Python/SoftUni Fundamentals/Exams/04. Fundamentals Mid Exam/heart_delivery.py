sequence_of_numbers = [int(x) for x in input().split('@')]

'''
[10, 10, 10, 2]
'''
successful_condition = True
last_position = 0
failed_count = 0

command = input()

while command != 'Love!':
    if command == 'Love!':
        break
    command = command.split()
    jump_length = int(command[1])

    for house in range(len(sequence_of_numbers)):
        current_index = house
        if jump_length > current_index:
            current_index = house
        if sequence_of_numbers[current_index] == 0:
            failed_count += 1
            successful_condition = False
            print(f"Place {current_index} already had Valentine's day.")
        current_index += jump_length
        sequence_of_numbers[current_index] -= 2
        if sequence_of_numbers[current_index] == 0:
            print(f"Place {current_index} has Valentine's day.")

        last_position = current_index
    command = input()

print(f"Cupid's last position was {last_position}.")

if successful_condition:
    print("Mission was successful.")
else:
    print(f"Cupid has failed {failed_count} places.")
# NOT DONE!
