# Sample

# command = input()
# lst = []
# while command != 'End':
#     if command == 'Paid':
#         print("\n".join(lst))
#         lst.clear()
#     else:
#         lst.append(command)
#
#     command = input()
# print("{} people remaining.".format(len(lst)))


# Using queue

from collections import deque

queue = deque()
command = input()
while command != 'End':
    if command == 'Paid':
        while queue:
            print(queue.popleft())
    else:
        queue.append(command)
    command = input()
print(f"{len(queue)} people remaining.")
