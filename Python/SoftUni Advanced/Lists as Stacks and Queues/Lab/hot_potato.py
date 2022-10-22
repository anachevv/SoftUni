from collections import deque

kids_names = deque(input().split())
n_toss = int(input())
count = 0
while len(kids_names) > 1:
    count += 1
    if count < n_toss:
        kids_names.append(kids_names.popleft())
    else:
        print("Removed {}".format(kids_names.popleft()))
        count = 0
print("Last is {}".format(kids_names.popleft()))
