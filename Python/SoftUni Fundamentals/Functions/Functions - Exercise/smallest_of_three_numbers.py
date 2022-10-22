def the_smallest_one(first_number=int(input()), second_number=int(input()), third_number=int(input())):

    lst = [first_number, second_number, third_number]
    min_number = min(lst)

    return min_number


print(the_smallest_one())
