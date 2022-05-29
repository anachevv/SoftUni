n_orders = int(input())
total_price = 0

for order in range(n_orders):
    price_per_capsule = float(input())
    days = int(input())
    daily_needed_capsules = int(input())

    if 0.01 <= price_per_capsule <= 100.00 and 1 <= days <= 31 and 1 <= daily_needed_capsules <= 2000:
        price = price_per_capsule * days * daily_needed_capsules
        total_price += price
        print(f'The price for the coffee is: ${price:.2f}')
    else:
        continue

print(f'Total: ${total_price:.2f}')
