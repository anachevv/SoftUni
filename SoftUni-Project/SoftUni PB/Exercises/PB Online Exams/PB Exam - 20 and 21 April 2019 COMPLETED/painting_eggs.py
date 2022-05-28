egg_size = input()
egg_colour = input()
batch_count = int(input())

price = 0
total_price = 0

if egg_size == "Large":
    if egg_colour == "Red":
        price = 16
    elif egg_colour == "Green":
        price = 12
    elif egg_colour == "Yellow":
        price = 9
elif egg_size == "Medium":
    if egg_colour == "Red":
        price = 13
    elif egg_colour == "Green":
        price = 9
    elif egg_colour == "Yellow":
        price = 7
elif egg_size == "Small":
    if egg_colour == "Red":
        price = 9
    elif egg_colour == "Green":
        price = 8
    elif egg_colour == "Yellow":
        price = 5

total_price = price * batch_count
total_price *= 0.65

print(f"{total_price:.2f} leva.")
