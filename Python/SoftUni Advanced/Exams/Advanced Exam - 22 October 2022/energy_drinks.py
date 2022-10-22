from collections import deque

numbers = [int(x) for x in input().split(', ')]
energy_drinks = deque([int(x) for x in input().split(', ')])
max_caffeine = 300
total_caffeine = 0

while numbers and energy_drinks:
    caffeine_dose = numbers.pop()
    drink = energy_drinks.popleft()
    result = caffeine_dose * drink

    if total_caffeine + result <= 300:
        total_caffeine += result
    else:
        energy_drinks.append(drink)
        if total_caffeine - 30 >= 0:
            total_caffeine -= 30


if energy_drinks:
    print(f"Drinks left: {', '.join(str(x) for x in energy_drinks)}")
else:
    print("At least Stamat wasn't exceeding the maximum caffeine.")

print(f"Stamat is going to sleep with {total_caffeine} mg caffeine.")
