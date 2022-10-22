sequence_of_words = input().split()

'''
['wow', 'father', 'mom', 'wow', 'shirt', 'stats']
'''

palindrome = input()

lst = [word for word in sequence_of_words if word[::-1] == word]

found_n_times = lst.count(palindrome)

print(lst)
print(f"Found palindrome {found_n_times} times")
