status_of_pirate_ship = [int(x) for x in input().split('>')]
status_of_warship = [int(y) for y in input().split('>')]
maximum_health = int(input())
stalemate = False

command = input()
while command != 'Retire':
    if stalemate:
        break

    if command == 'Retire':
        break

    command = command.split()

    if 'Fire' in command:
        index = int(command[1])
        damage = int(command[2])
        if -1 < index < len(status_of_warship):
            status_of_warship[index] -= damage
            if status_of_warship[index] <= 0:
                stalemate = True
                print("You won! The enemy ship has sunken.")
                break

    elif 'Defend' in command:
        start_index = int(command[1])
        end_index = int(command[2])
        damage = int(command[3])
        if -1 < start_index < len(status_of_pirate_ship) and -1 < end_index < len(status_of_pirate_ship):
            for i in status_of_pirate_ship:
                status_of_pirate_ship[start_index] -= damage
                if status_of_pirate_ship[start_index] <= 0:
                    stalemate = True
                    print("You lost! The pirate ship has sunken.")
                    break
                if start_index == end_index:
                    break
                start_index += 1

    elif 'Repair' in command:
        index = int(command[1])
        health = int(command[2])
        if -1 < index < len(status_of_pirate_ship):
            status_of_pirate_ship[index] += health
            if status_of_pirate_ship[index] > maximum_health:
                status_of_pirate_ship[index] = maximum_health

    elif 'Status' in command:
        percentage = 0.2 * maximum_health
        count = len([x for x in status_of_pirate_ship if x < percentage])
        print(f'{count} sections need repair.')

    command = input()

if not stalemate:
    sum_of_pirate_ship = sum(status_of_pirate_ship)
    sum_of_warship = sum(status_of_warship)
    print(f"Pirate ship status: {sum_of_pirate_ship}")
    print(f"Warship status: {sum_of_warship}")
