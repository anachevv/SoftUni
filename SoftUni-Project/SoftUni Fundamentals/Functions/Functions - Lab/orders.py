def orders(product=input(), quantity=int(input())):

    coffee_price = 1.5
    water_price = 1
    coke_price = 1.4
    snacks_price = 2

    result = 0

    if product == 'coffee':
        result = coffee_price * quantity
    if product == 'water':
        result = water_price * quantity
    if product == 'coke':
        result = coke_price * quantity
    if product == 'snacks':
        result = snacks_price * quantity

    return f'{result:.2f}'


print(orders())
