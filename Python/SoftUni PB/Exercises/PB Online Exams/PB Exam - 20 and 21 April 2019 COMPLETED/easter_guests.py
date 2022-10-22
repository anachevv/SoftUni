import math

guests = int(input())
budget = float(input())
easter_bread_price = 4
egg_price = 0.45
needed_easter_breads = math.ceil(guests / 3)
needed_eggs = guests * 2

total_price = needed_easter_breads * easter_bread_price + needed_eggs * egg_price

if budget >= total_price:
    remaining_money = budget - total_price
    print(f"Lyubo bought {needed_easter_breads} Easter bread and {needed_eggs} eggs.\n"
          f"He has {remaining_money:.2f} lv. left.")
else:
    needed_money = total_price - budget
    print(f"Lyubo doesn't have enough money.\nHe needs {needed_money:.2f} lv. more.")
