from collections import deque

working_bees = deque([int(x) for x in input().split()])
nectar_values = [int(x) for x in input().split()]
honey_process = deque(input().split())

operators = {'-': lambda a, b: a - b, '+': lambda a, b: a + b, '*': lambda a, b: a * b, '/': lambda a, b: a / b}

total_nectar = 0
while nectar_values and working_bees:
    bee = working_bees.popleft()
    nectar = nectar_values.pop()
    if bee > nectar:
        working_bees.appendleft(bee)
        continue
    if nectar == 0:
        continue
    else:
        operator = honey_process.popleft()
        total_nectar += abs(operators[operator](bee, nectar))

print(f"Total honey made: {total_nectar}")
if working_bees:
    print(f"Bees left: {', '.join(str(x) for x in working_bees)}")
if nectar_values:
    print(f"Nectar left: {', '.join(str(x) for x in nectar_values)}")
