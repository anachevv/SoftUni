sequence_of_numbers = input().split()
sequence_of_numbers = [int(x) for x in sequence_of_numbers]

is_even = lambda x: x % 2 == 0

filtered_list = list(filter(is_even, sequence_of_numbers))

print(filtered_list)
