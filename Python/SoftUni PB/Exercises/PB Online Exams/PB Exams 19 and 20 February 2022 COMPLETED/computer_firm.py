n_computers = int(input())
possible_sales = 0
rating_two = 0
rating_three = 0
rating_four = 0
rating_five = 0
rating_six = 0
total = 0

for current_numbers in range(n_computers):
    sales_and_rating_number = int(input())
    string_sales_and_rating_number = str(sales_and_rating_number)

    string_rating = string_sales_and_rating_number[-1]

    hundreds = string_sales_and_rating_number[0]
    tens = string_sales_and_rating_number[1]

    total = int(hundreds + tens)

    if string_rating == "2":
        possible_sales += 0
        rating_two += 1
    elif string_rating == "3":
        possible_sales += 0.5 * total
        rating_three += 1
    elif string_rating == "4":
        possible_sales += 0.7 * total
        rating_four += 1
    elif string_rating == "5":
        possible_sales += 0.85 * total
        rating_five += 1
    elif string_rating == "6":
        possible_sales += total
        rating_six += 1

total_rating = 2 * rating_two + 3 * rating_three + 4 * rating_four + 5 * rating_five + 6 * rating_six
average_rating = total_rating / n_computers

print(f"{possible_sales:.2f}")
print(f"{average_rating:.2f}")
