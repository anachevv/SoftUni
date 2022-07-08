number = int(input())
is_prime = False

for i in range(2, number):
    if (number % i) == 0:
        is_prime = True
        break

if is_prime:
    print('False')
else:
    print('True')
