n_number = int(input())
special_number = False

for current_number in range(1, n_number + 1):
    total_sum = 0
    for x in str(current_number):
        total_sum += int(x)
    if total_sum == 5 or total_sum == 7 or total_sum == 11:
        special_number = True
    else:
        special_number = False
    print(f'{current_number} -> {special_number}')
