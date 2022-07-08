sequence_of_names = input().split(', ')
sorted_lst = sorted(sequence_of_names, key=lambda x: (-len(x), x))

print(sorted_lst)
