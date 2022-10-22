n = int(input())
numbers_list = []

for x in range(0, n):
    number = int(input())
    numbers_list.append(number)

max_number = max(numbers_list)
total_sum = sum(numbers_list) - max_number
diff = abs(total_sum - max_number)

if max_number == total_sum:
    print(f"Yes\nSum = {total_sum}")
else:
    print(f"No\nDiff = {diff}")
