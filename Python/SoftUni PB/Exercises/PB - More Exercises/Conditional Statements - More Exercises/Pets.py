import math

days = int(input())
total_food_kg = int(input())
daily_food_kg_dog = float(input())
daily_food_kg_cat = float(input())
daily_food_kg_turtle_grams = float(input())

food_dog_kg = daily_food_kg_dog * days
food_cat_kg = daily_food_kg_cat * days
food_turtle_grams = daily_food_kg_turtle_grams * days / 1000
total_food = food_dog_kg + food_cat_kg + food_turtle_grams

if total_food_kg >= total_food:
    remainder = math.floor(total_food_kg - total_food)
    print(f"{remainder} kilos of food left.")
elif total_food_kg < total_food:
    remainder = math.ceil(total_food - total_food_kg)
    print(f"{remainder} more kilos of food are needed.")
