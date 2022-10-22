n_lines = int(input())
word = input()

total_lst = [input() for current_word in range(n_lines)]

special_lst = [x for x in total_lst if x.find(word) != -1]

print(total_lst)

print(special_lst)
