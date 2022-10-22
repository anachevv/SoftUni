command = input()
info = {}
while command != "EndDay":
    command = command.split(': ')
    if 'Add' in command:
        current_command = command[-1].split('-')
        name, needed_food, area = current_command[0], int(current_command[1]), current_command[2]
        if name not in info:
            info[name] = [0, area]
        info[name][0] += needed_food
    elif 'Feed' in command:
        current_command = command[-1].split('-')
        name, food = current_command[0], int(current_command[1])
        if name in info:
            info[name][0] -= food
            if info[name][0] <= 0:
                print(f"{name} was successfully fed")
                del info[name]
    command = input()

areas = {}
print('Animals:')
for name, info in info.items():
    current_area = info[-1]
    if current_area not in areas:
        areas[current_area] = 0
    areas[current_area] += 1
    print(f" {name} -> {info[0]}g")

print("Areas with hungry animals:")
for area, number in areas.items():
    print(f" {area}: {number}")
