string = input().split(', ')
beggars_count = int(input())

sums = [int(element) for element in string]
final_sums = []
index = 0

while index < beggars_count:
    current_sum = 0

    for current_index in range(index, len(sums), beggars_count):
        current_sum += sums[current_index]

    index += 1

    final_sums.append(current_sum)

print(final_sums)
