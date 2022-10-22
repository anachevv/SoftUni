n_lines = int(input())

lst = [int(input()) for i in range(n_lines)]

command = input()

even_lst = [x for x in lst if x % 2 == 0]
odd_lst = [y for y in lst if y % 2 != 0]
negative_lst = [z for z in lst if z < 0]
positive_lst = [j for j in lst if j >= 0]

if command == 'even':
    print(even_lst)
elif command == 'odd':
    print(odd_lst)
elif command == 'negative':
    print(negative_lst)
elif command == 'positive':
    print(positive_lst)
