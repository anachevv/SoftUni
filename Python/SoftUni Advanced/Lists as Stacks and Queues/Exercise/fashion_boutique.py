stack = [int(num) for num in input().split()]
capacity = int(input())
current_capacity = capacity
racks = 1
while stack:
    if stack[-1] > current_capacity:
        racks += 1
        current_capacity = capacity
    else:
        current_capacity -= stack[-1]
        stack.pop()
print(racks)
