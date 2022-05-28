decorations_quantity = int(input())
remaining_days = int(input())
total_price = 0
christmas_spirit = 0

ornament_set_price = 2
tree_skirt_price = 5
tree_garland_price = 3
tree_lights_price = 15

for day in range(1, remaining_days + 1):
    if day % 11 == 0:
        decorations_quantity += 2
    if day % 2 == 0:
        total_price += decorations_quantity * ornament_set_price
        christmas_spirit += 5
    if day % 3 == 0:
        total_price += (tree_skirt_price + tree_garland_price) * decorations_quantity
        christmas_spirit += 13
    if day % 5 == 0:
        total_price += decorations_quantity * 15
        christmas_spirit += 17
        if day % 3 == 0:
            christmas_spirit += 30
    if day % 10 == 0:
        christmas_spirit -= 20
        total_price += 23

if remaining_days % 10 == 0:
    christmas_spirit -= 30

print(f"Total cost: {total_price}")
print(f"Total spirit: {christmas_spirit}")
