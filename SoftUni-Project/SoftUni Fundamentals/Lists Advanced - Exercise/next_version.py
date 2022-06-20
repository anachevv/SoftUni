lst = [int(x) for x in input().split('.')]

lst[-1] += 1

for number in range(len(lst) - 1, -1, -1):
    if lst[number] > 9:
        lst[number] = 0
        lst[number - 1] += 1

print('.'.join(str(x) for x in lst))
