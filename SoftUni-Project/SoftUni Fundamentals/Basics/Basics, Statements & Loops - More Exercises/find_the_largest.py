number = int(input())

lst = [char for char in str(number)]

lst.sort(reverse=True)

number = ''.join(i for i in lst)

print(int(number))
