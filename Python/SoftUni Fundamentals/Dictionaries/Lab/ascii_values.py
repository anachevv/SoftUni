list_of_characters = input().split(', ')

dct = {key: ord(key) for key in list_of_characters}
print(dct)

# Using for-loop

# dct = {}
# for char in range(len(list_of_characters)):
#     key = list_of_characters[char]
#     value = ord(list_of_characters[char])
#     dct[key] = value
#
# print(dct)
