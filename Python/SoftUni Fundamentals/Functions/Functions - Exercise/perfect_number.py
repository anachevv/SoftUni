def perfect_number(num):

    for i in range(1, num):
        if num % i == 0:
            lst.append(i)

    return lst


number = int(input())

lst = []
sum = sum(perfect_number(number))

if sum == number:
    print("We have a perfect number!")
else:
    print("It's not so perfect.")
