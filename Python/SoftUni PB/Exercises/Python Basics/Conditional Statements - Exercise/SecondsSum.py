first = int(input())
second = int(input())
third = int(input())

sum1 = first + second + third

minutes = sum1 // 60
seconds = sum1 % 60

if seconds < 10:
    print(str(minutes) + ":0" + str(seconds))
else:
    print(str(minutes) + ":" + str(seconds))