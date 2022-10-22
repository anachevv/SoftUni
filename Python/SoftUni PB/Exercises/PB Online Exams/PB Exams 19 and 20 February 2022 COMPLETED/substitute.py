first_player_first_digit = int(input())
first_player_second_digit = int(input())

second_player_first_digit = int(input())
second_player_second_digit = int(input())

change_counter = 0

for first_digit in range(first_player_first_digit, 8 + 1):
    for second_digit in range(9, first_player_second_digit - 1, -1):
        for third_digit in range(second_player_first_digit, 8 + 1):
            for fourth_digit in range(9, second_player_second_digit - 1, -1):

                if first_digit % 2 == 0 and third_digit % 2 == 0 and second_digit % 2 != 0 and fourth_digit % 2 != 0:
                    if first_digit == third_digit and \
                            second_digit == fourth_digit:
                        print("Cannot change the same player.")
                    else:
                        print(f"{first_digit}{second_digit} - "
                              f"{third_digit}{fourth_digit}")
                        change_counter += 1

                if change_counter == 6:
                    break
            if change_counter == 6:
                break
        if change_counter == 6:
            break
    if change_counter == 6:
        break
