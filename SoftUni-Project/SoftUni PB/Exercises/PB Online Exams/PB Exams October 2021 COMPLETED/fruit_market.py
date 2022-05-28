strawberries_price = float(input())
bananas_quantity = float(input())
oranges_quantity = float(input())
raspberries_quantity = float(input())
strawberries_quantity = float(input())

raspberries_price = 1/2 * strawberries_price
oranges_price = 0.6 * raspberries_price
bananas_price = 0.2 * raspberries_price

total_price = strawberries_price * strawberries_quantity + raspberries_price * raspberries_quantity + oranges_price * \
              oranges_quantity + bananas_price * bananas_quantity

print(f"{total_price:.2f}")
