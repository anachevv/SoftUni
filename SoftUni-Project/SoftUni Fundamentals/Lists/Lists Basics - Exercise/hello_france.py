items_and_prices = input().split('|')
budget = float(input())
first_budget = budget

train_ticket_price = 150

new_budget = 0

for item in range(len(items_and_prices)):

    new_price = 0
    item_type, price = items_and_prices[item].split('->')
    price = float(price)
    if budget < price:
        continue
    if item_type == 'Clothes':
        if price <= 50:
            budget -= price
            new_price = price + price * 0.4
    elif item_type == 'Shoes':
        if price <= 35:
            budget -= price
            new_price = price + price * 0.4
    elif item_type == 'Accessories':
        if price <= 20.25:
            budget -= price
            new_price = price + price * 0.4

    new_budget += new_price

    if new_price > 0.00:
        print(f'{new_price:.2f}', end=' ')

new_budget += budget

profit = new_budget - first_budget

print(f'\nProfit: {profit:.2f}')

if new_budget >= train_ticket_price:
    print('Hello, France!')
else:
    print('Not enough money.')
