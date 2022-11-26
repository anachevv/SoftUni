from itertools import permutations


def possible_permutations(lst):
    for i in list(permutations(lst)):
        yield list(i)


[print(n) for n in possible_permutations([1, 2, 3])]

print()

[print(n) for n in possible_permutations([1])]
