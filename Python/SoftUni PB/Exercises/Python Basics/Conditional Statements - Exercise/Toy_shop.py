excursion_price = float(input())

puzzles_amount = int(input())
speaking_dolls_amount = int(input())
teddy_bear_amount = int(input())
minions_amount = int(input())
toy_truck_amount = int(input())

puzzle_price = 2.6 * puzzles_amount
speaking_doll_price = 3 * speaking_dolls_amount
teddy_bear_price = 4.1 * teddy_bear_amount
minion_price = 8.2 * minions_amount
toy_truck_price = 2 * toy_truck_amount

profit = 0

total_toy_amount = puzzles_amount + speaking_dolls_amount + \
    teddy_bear_amount + minions_amount + toy_truck_amount

toy_price = puzzle_price + speaking_doll_price + teddy_bear_price  \
            + minion_price + toy_truck_price

if total_toy_amount >= 50:
    discount = 0.25 * toy_price
else:
    discount = 0
total_price = toy_price - discount
rent = total_price * 0.1
profit = total_price - rent
remaining_money = abs(profit - excursion_price)
if profit >= excursion_price:
    print(f"Yes! {remaining_money:.2f} lv left.")
else:
    print(f"Not enough money! {remaining_money:.2f} lv needed.")
