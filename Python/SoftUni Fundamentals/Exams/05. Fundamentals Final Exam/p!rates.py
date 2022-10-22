command = input()
cities = {}

while command != "Sail":
    command = command.split('||')
    city, population, gold = command[0], int(command[1]), int(command[2])
    if city not in cities:
        cities[city] = [0, 0]
    cities[city][0] += population
    cities[city][1] += gold
    command = input()

command = input()

while command != 'End':
    command = command.split('=>')
    if 'Plunder' in command:
        town, people, gold = command[1], int(command[2]), int(command[3])
        cities[town][0] -= people
        cities[town][1] -= gold
        if cities[town][0] <= 0 or cities[town][1] <= 0:
            print(f"{town} plundered! {gold} gold stolen, {people} citizens killed.")
            cities.pop(town)
            print(f"{town} has been wiped off the map!")
        else:
            print(f"{town} plundered! {gold} gold stolen, {people} citizens killed.")
    elif 'Prosper' in command:
        town, gold = command[1], int(command[2])
        if gold < 0:
            print("Gold added cannot be a negative number!" )
        else:
            cities[town][1] += gold
            print(f"{gold} gold added to the city treasury. {town} now has {cities[town][1]} gold.")

    command = input()

if cities:
    count = len(cities)
    print(f"Ahoy, Captain! There are {count} wealthy settlements to go to:")
    for city, value in cities.items():
        pop = value[0]
        gold = value[1]
        print(f"{city} -> Population: {pop} citizens, Gold: {gold} kg")
else:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")
