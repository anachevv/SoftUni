from collections import deque

food_quantity = int(input())
queue = deque([int(num) for num in input().split()])
orders_complete = True
max_order = -100000
for order in queue:
    if order > max_order:
        max_order = order
print(max_order)

while queue:
    if queue[0] <= food_quantity:
        food_quantity -= queue[0]
        queue.popleft()
    else:
        orders_complete = False
        break
if not orders_complete:
    print(f"Orders left: {' '.join(str(x) for x in queue)}")
else:
    print(f"Orders complete")
