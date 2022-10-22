number_of_electrons = int(input())
lst = []
count = 1
while sum(lst) != number_of_electrons:
    element = 2 * (count ** 2)

    if element < number_of_electrons:
        number_of_electrons -= element
        lst.append(element)
    else:
        lst.append(number_of_electrons)
        break
    count += 1

print(lst)
