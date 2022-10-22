money_in_pocket_per_day = float(input())
earned_money_per_day = float(input())
total_outcome = float(input())
gift_price = float(input())
days = 5

total_money = (days * money_in_pocket_per_day + 5 * earned_money_per_day) - total_outcome

if total_money >= gift_price:
    print(f"Profit: {total_money:.2f} BGN, the gift has been purchased.")
else:
    needed_money = gift_price - total_money
    print(f"Insufficient money: {needed_money:.2f} BGN.")
