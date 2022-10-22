from collections import deque

water_quantity = int(input())
name = input()
queue = deque()
while name != 'Start':
    queue.append(name)
    name = input()

command = input()
while command != 'End':
    if 'refill' in command:
        liters_to_add = int(command.split()[1])
        water_quantity += liters_to_add
    else:
        liters_to_give = int(command)
        if liters_to_give <= water_quantity:
            water_quantity -= liters_to_give
            print(f"{queue[0]} got water")
            queue.popleft()
        else:
            print(f"{queue[0]} must wait")
            queue.popleft()
    command = input()
print(f"{water_quantity} liters left")
