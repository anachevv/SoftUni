string = input()

lst = []

for index, char in enumerate(string):
    if char.isalpha():
        if char.upper() == char:
            lst.append(index)

print(lst)
