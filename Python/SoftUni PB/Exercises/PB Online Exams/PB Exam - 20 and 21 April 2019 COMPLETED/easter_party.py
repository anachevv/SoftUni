guests = int(input())
price_per_guest = float(input())
budget = float(input())
cake_price = 0.1 * budget

if 10 <= guests <= 15:
    price_per_guest *= 0.85
elif 15 < guests <= 20:
    price_per_guest *= 0.8
elif guests > 20:
    price_per_guest *= 0.75

total_price = price_per_guest * guests + cake_price

if budget >= total_price:
    remaining_money = budget - total_price
    print(f"It is party time! {remaining_money:.2f} leva left.")
else:
    needed_money = total_price - budget
    print(f"No party! {needed_money:.2f} leva needed.")
