def min_max_sum(numbers):

    return f"The minimum number is {min(numbers)}\nThe maximum number is {max(numbers)}\nThe sum number is: {sum(numbers)}"


sequence_of_numbers = [int(char) for char in input().split()]

print(min_max_sum(sequence_of_numbers))
