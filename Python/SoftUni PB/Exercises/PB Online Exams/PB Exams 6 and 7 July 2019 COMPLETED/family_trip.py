budget = float(input())
overnights = int(input())
overnight_price = float(input())
outcome_percent = int(input())

if overnights > 7:
    overnight_price *= 0.95

total_price = overnights * overnight_price + outcome_percent / 100 * budget
remaining_money = abs(budget - total_price)

if budget >= total_price:
    print(f"Ivanovi will be left with {remaining_money:.2f} leva after vacation.")
else:
    print(f"{remaining_money:.2f} leva needed.")
