start_number = input()
end_number = input()

for number_one in range(int(start_number[0]), int(end_number[0]) + 1):
    for number_two in range(int(start_number[1]), int(end_number[1]) + 1):
        for number_three in range(int(start_number[2]), int(end_number[2]) + 1):
            for number_four in range(int(start_number[3]), int(end_number[3]) + 1):
                if number_one % 2 != 0 and number_two % 2 != 0 and number_three % 2 != 0 and number_four % 2 != 0:
                    print(f"{number_one}{number_two}{number_three}{number_four}", end=" ")
