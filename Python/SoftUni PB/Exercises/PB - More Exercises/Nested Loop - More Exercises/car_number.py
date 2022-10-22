start_range = int(input())
end_range = int(input())

for first_digit in range(start_range, end_range + 1):
    if first_digit % 2 == 0:
        for second_digit in range(start_range, end_range + 1):
            for third_digit in range(start_range, end_range + 1):
                for fourth_digit in range(start_range, end_range + 1):
                    necessary_sum = second_digit + third_digit

                    if fourth_digit % 2 != 0:
                        if first_digit > fourth_digit:
                            if necessary_sum % 2 == 0:
                                print(f"{first_digit}{second_digit}{third_digit}{fourth_digit}", end=" ")

    elif first_digit % 2 != 0:
        for second_digit in range(start_range, end_range + 1):
            for third_digit in range(start_range, end_range + 1):
                for fourth_digit in range(start_range, end_range + 1):
                    necessary_sum = second_digit + third_digit

                    if fourth_digit % 2 == 0:
                        if first_digit > fourth_digit:
                            if necessary_sum % 2 == 0:
                                print(f"{first_digit}{second_digit}{third_digit}{fourth_digit}", end=" ")
