numbers = list(map(int, input().split()))
target_number = int(input())
unique_pairs = []
iterations = 0
for first_number in range(len(numbers)):
    for second_number in range(first_number + 1, len(numbers)):
        iterations += 1
        if first_number + second_number == target_number:
            print(f"{first_number} + {second_number} = {target_number}")
            unique_pairs.append((first_number, second_number))
unique_pairs = set(unique_pairs)
print(f"Iterations done: {iterations}")
