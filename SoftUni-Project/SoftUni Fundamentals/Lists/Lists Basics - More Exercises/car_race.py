sequence_of_numbers = [int(i) for i in input().split()]

finish = len(sequence_of_numbers) // 2

left_side = sequence_of_numbers[:finish]
right_side = sequence_of_numbers[-1:finish:-1]

first_time = 0
second_time = 0

for left_number in left_side:

    first_time += left_number

    if left_number == 0:
        first_time *= 0.8


for right_number in right_side:

    second_time += right_number

    if right_number == 0:
        second_time *= 0.8

if first_time < second_time:
    print(f"The winner is left with total time: {first_time:.1f}")
else:
    print(f"The winner is right with total time: {second_time:.1f}")
