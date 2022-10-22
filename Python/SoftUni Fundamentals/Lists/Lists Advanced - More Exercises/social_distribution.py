sequence_of_population = [int(element) for element in input().split(', ')]
minimum_wealth = int(input())

max_wealth = max(sequence_of_population)
index_of_max_wealth = sequence_of_population.index(max_wealth)
difference_sum = 0

condition = False

for wealth in sequence_of_population:
    if wealth < minimum_wealth:
        sequence_of_population[sequence_of_population.index(wealth)] += (minimum_wealth - wealth)
        sequence_of_population[sequence_of_population.index(max(sequence_of_population))] -= (minimum_wealth - wealth)

for x in sequence_of_population:
    if x < minimum_wealth:
        condition = True

if condition:
    print("No equal distribution possible")
else:
    print(sequence_of_population)


# Using a function


# def distribution(sequence, min_wealth):
#
#     for wealth in sequence:
#         if wealth < min_wealth:
#             sequence[sequence.index(wealth)] += (min_wealth - wealth)
#             sequence[sequence.index(max(sequence))] -= (min_wealth - wealth)
#
#     return sequence
#
#
# sequence_of_population = [int(element) for element in input().split(', ')]
# minimum_wealth = int(input())
#
#
# distribution(sequence_of_population, minimum_wealth)
#
#
# condition = False
#
# for x in sequence_of_population:
#     if x < minimum_wealth:
#         condition = True
#
# if condition:
#     print("No equal distribution possible")
# else:
#     print(sequence_of_population)
