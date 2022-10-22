import math

absence_days = int(input())
prepared_food = int(input())
food_per_day_of_the_first_one = float(input())
food_per_day_of_the_second_one = float(input())
food_per_day_of_the_third_one = float(input())

total_needed_food = food_per_day_of_the_first_one * absence_days + food_per_day_of_the_second_one * absence_days + \
                    food_per_day_of_the_third_one * absence_days
if prepared_food >= total_needed_food:
    remaining_food = prepared_food - total_needed_food
    print(f"{math.floor(remaining_food)} kilos of food left.")
else:
    needed_food = total_needed_food - prepared_food
    print(f"{math.ceil(needed_food)} more kilos of food are needed.")
