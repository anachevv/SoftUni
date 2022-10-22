flour_price = float(input())
flour_quantity = float(input())
sugar_quantity = float(input())
eggshells_quantity = int(input())
yeats_quantity = int(input())

flour_total_price = flour_price * flour_quantity
sugar_price = 0.75 * flour_price * sugar_quantity
eggshells_price = 1.10 * flour_price * eggshells_quantity
yeats_price = 0.2 * sugar_price * yeats_quantity / sugar_quantity

total_price = flour_total_price + sugar_price + eggshells_price + yeats_price

print(f"{total_price:.2f}")
