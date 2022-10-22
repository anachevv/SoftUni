user_input = input().split()
count = int(input())

lst = [int(i) for i in user_input]

for number in range(count):
    lst.remove(min(lst))

for number in lst:
    if number != lst[-1]:
        print(number, end=', ')
    else:
        print(number)
