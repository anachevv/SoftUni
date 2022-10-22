days = int(input())
total_food = float(input())
dog_total_food = 0
cat_total_food = 0
total_biscuits = 0

for x in range(1, days + 1):
    current_dog_food = int(input())
    current_cat_food = int(input())

    dog_total_food += current_dog_food
    cat_total_food += current_cat_food

    if x % 3 == 0:
        total_biscuits += 0.1 * (current_dog_food + current_cat_food)

print(f"Total eaten biscuits: {round(total_biscuits)}gr.")
print(f"{(dog_total_food + cat_total_food) / total_food * 100:.2f}% of the food has been eaten.")
print(f"{dog_total_food / (dog_total_food + cat_total_food) * 100:.2f}% eaten from the dog.")
print(f"{cat_total_food / (dog_total_food + cat_total_food) * 100:.2f}% eaten from the cat.")
