n_numbers = int(input())
total_sum = 0

for numbers in range(n_numbers):
    current_number = int(input())
    total_sum += current_number

average_sum = total_sum / n_numbers

print(f"{average_sum:.2f}")
