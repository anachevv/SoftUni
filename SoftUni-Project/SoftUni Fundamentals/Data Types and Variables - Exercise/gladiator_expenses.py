losses = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

total_price = 0

for loss in range(1, losses + 1):

    if loss % 2 == 0:
        total_price += helmet_price
    if loss % 3 == 0:
        total_price += sword_price
    if loss % 6 == 0:
        total_price += shield_price
    if loss % 12 == 0:
        total_price += armor_price

print(f"Gladiator expenses: {total_price:.2f} aureus")
