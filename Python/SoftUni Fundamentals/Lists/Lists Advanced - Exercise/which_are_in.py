first_sequence_of_strings = input().split(', ')
second_sequence_of_strings = input().split(', ')

lst = []

for x in first_sequence_of_strings:
    for y in second_sequence_of_strings:
        if x in y and x not in lst:
            lst.append(x)

print(lst)
