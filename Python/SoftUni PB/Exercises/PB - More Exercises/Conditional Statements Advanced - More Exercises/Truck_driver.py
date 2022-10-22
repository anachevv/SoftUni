season = input()
distance = float(input())
price = 0

if distance <= 5000:
    if season == "Spring" or season == "Autumn":
        price = 0.75 * distance * 4
    elif season == "Summer":
        price = 0.9 * distance * 4
    elif season == "Winter":
        price = 1.05 * distance * 4

elif 5000 < distance <= 10000:
    if season == "Spring" or season == "Autumn":
        price = 0.95 * distance * 4
    elif season == "Summer":
        price = 1.1 * distance * 4
    elif season == "Winter":
        price = 1.25 * distance * 4

elif 10000 < distance <= 20000:
    price = 1.45 * distance * 4

price *= 0.9

print(f"{price:.2f}")
