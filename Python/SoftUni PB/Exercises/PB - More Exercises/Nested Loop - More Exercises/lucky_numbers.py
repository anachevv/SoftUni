number = int(input())

for first in range(1, 9 + 1):
    for second in range(1, 9 + 1):
        for third in range(1, 9 + 1):
            for fourth in range(1, 9 + 1):
                first_sum = first + second
                second_sum = third + fourth
                if first_sum == second_sum:
                    if number % first_sum == 0:
                        print(f"{first}{second}{third}{fourth}", end=" ")
