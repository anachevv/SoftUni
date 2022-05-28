age = int(input())
washing_machine_price = float(input())
toy_price = int(input())

toys_amount = 0
received_money = 0
total_money = 0

for x in range(1, age + 1):
    if x % 2 == 0:
        received_money += (10 * (x / 2)) - 1
    else:
        toys_amount += 1

total_money = received_money + toy_price * toys_amount

if total_money >= washing_machine_price:
    remaining_money = total_money - washing_machine_price
    print(f"Yes! {remaining_money:.2f}")
else:
    needed_money = washing_machine_price - total_money
    print(f"No! {needed_money:.2f}")
