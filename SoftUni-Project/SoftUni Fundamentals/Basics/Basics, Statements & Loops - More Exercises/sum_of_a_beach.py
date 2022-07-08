word = input().lower()

lst = ['sand', 'water', 'fish', 'sun']

count = [word.count(lst[x]) for x in range(len(lst))]

count_sum = sum(count)

print(count_sum)
