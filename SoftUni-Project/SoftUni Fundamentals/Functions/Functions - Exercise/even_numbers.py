# sequence_of_numbers = input().split()
# sequence_of_numbers = [int(x) for x in sequence_of_numbers]
#
# is_even = lambda x: x % 2 == 0
#
# filtered_list = list(filter(is_even, sequence_of_numbers))
#
# print(filtered_list)


def is_even(number):
    if int(number) % 2 == 0:
        return True
    return False


numbers = input().split()
filtered_numbers = []

for current_number in numbers:
    if is_even(current_number):
        filtered_numbers.append(int(current_number))

print(filtered_numbers)
