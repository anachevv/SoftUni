# def sort():
#
#     for number in sequence_of_numbers:
#         sorted_list.append(int(number))
#
#     return sorted(sorted_list)
#
#
# sequence_of_numbers = input().split()
# sorted_list = []
#
# print(sort())


def sort(nums):

    return sorted(nums)


sequence_of_numbers = input().split()
numbers = [int(x) for x in sequence_of_numbers]

print(sort(numbers))
