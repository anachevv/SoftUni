water_quantity = int(input())
name = input()
queue = []
while name != 'Start':
    queue.append(name)
    name = input()

command = input()
person = 0
while command != 'End':
    if 'refill' in command:
        liters_to_add = int(command.split()[1])
        water_quantity += liters_to_add
    else:
        liters_to_give = int(command)
        if liters_to_give <= water_quantity:
            water_quantity -= liters_to_give
            print(f"{queue[person]} got water")
            queue.remove(queue[person])
        else:
            print(f"{queue[person]} must wait")
            queue.remove(queue[person])
    command = input()
print(f"{water_quantity} liters left")
