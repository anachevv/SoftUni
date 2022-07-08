health = 100
bitcoins = 0
sequence_of_rooms = input().split('|')
player_is_killed = False
room_number = 0

for x in range(len(sequence_of_rooms)):
    rooms = sequence_of_rooms[x]
    rooms = rooms.split()
    room_number += 1
    command = rooms[0]
    number = int(rooms[1])

    if command == 'potion':
        current_health = health
        health += number
        if health > 100:
            health = 100
        print(f'You healed for {abs(health - current_health)} hp.')
        print(f'Current health: {health} hp.')
    elif command == 'chest':
        bitcoins += number
        print(f'You found {number} bitcoins.')
    else:
        health -= number
        if health > 0:
            print(f'You slayed {command}.')
        else:
            player_is_killed = True
            print(f"You died! Killed by {command}.")
            print(f"Best room: {room_number}")
            break

if not player_is_killed:
    print("You've made it!")
    print(f"Bitcoins: {bitcoins}")
    print(f"Health: {health}")
