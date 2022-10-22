from collections import deque

petrol_pumps = int(input())
queue = deque()
for _ in range(petrol_pumps):
    queue.append([int(element) for element in input().split()])

for pump_index in range(petrol_pumps):
    tank = 0
    failed = False
    for petrol, distance in queue:
        tank += petrol - distance
        if tank < 0:
            failed = True
            break
    if failed:
        queue.append(queue.popleft())
    else:
        print(pump_index)
        break
