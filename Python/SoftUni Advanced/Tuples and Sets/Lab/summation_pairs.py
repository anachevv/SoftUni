numbers = list(map(int, input().split()))
target_number = int(input())
unique_pairs = []
iterations = 0
for first_number in range(len(numbers)):
    for second_number in range(first_number + 1, len(numbers)):
        iterations += 1
        if numbers[first_number] + numbers[second_number] == target_number:
            print(f"{numbers[first_number]} + {numbers[second_number]} = {target_number}")
            unique_pairs.append((numbers[first_number], numbers[second_number]))
unique_pairs = set(unique_pairs)
print(f"Iterations done: {iterations}")
print('\n'.join(str(x) for x in unique_pairs))
