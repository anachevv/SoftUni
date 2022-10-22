fats_percent = int(input()) / 100
proteins_percent = int(input()) / 100
carbohydrates_percent = int(input()) / 100
total_calories = int(input())
water_percent = int(input()) / 100

fats_grams = fats_percent * total_calories / 9
proteins_grams = proteins_percent * total_calories / 4
carbohydrates_grams = carbohydrates_percent * total_calories / 4

total_food = fats_grams + proteins_grams + carbohydrates_grams

calories_per_gram = total_calories / total_food

total_calories = (1 - water_percent) * calories_per_gram

print(f"{total_calories:.4f}")
