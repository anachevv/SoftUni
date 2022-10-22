products_and_prices = {}
command = input()

while command != "buy":
    name, price, quantity = command.split()
    price = float(price)
    quantity = int(quantity)

    if name not in products_and_prices:
        products_and_prices[name] = [price, quantity]
    else:
        products_and_prices[name][0] = price
        products_and_prices[name][1] += quantity

    command = input()

for key, value in products_and_prices.items():
    total_price = value[0] * value[1]
    print(f"{key} -> {total_price:.2f}")
