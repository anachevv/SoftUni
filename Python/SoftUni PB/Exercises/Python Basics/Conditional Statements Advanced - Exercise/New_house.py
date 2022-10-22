type_flowers = input()
amount = int(input())
budget = int(input())

roses = 5
dahlias = 3.8
tulips = 2.8
narcissus = 3
gladiolus = 2.5

price = 0
discount = 0
total_price = 0

if type_flowers == "Roses":
    if amount > 80:
        price = 5 * amount
        discount = 0.1 * price
        total_price = price - discount
    else:
        discount = 0
        price = 5 * amount
        total_price = price - discount
elif type_flowers == "Dahlias":
    if amount > 90:
        price = 3.8 * amount
        discount = 0.15 * price
        total_price = price - discount
    else:
        discount = 0
        price = 3.8 * amount
        total_price = price - discount
elif type_flowers == "Tulips":
    if amount > 80:
        price = 2.8 * amount
        discount = 0.15 * price
        total_price = price - discount
    else:
        discount = 0
        price = 2.8 * amount
        total_price = price - discount
elif type_flowers == "Narcissus":
    if amount < 120:
        price = 3 * amount
        discount = 0.15 * price
        total_price = price + discount
    else:
        discount = 0
        price = 3 * amount
        total_price = price - discount
elif type_flowers == "Gladiolus":
    if amount < 80:
        price = 2.5 * amount
        discount = 0.2 * price
        total_price = price + discount
    else:
        discount = 0
        price = 2.5 * amount
        total_price = price - discount

remaining_money = abs(budget - total_price)

if budget >= total_price:
    print(f"Hey, you have a great garden with {amount} {type_flowers} "
          f"and {remaining_money:.2f} leva left.")
else:
    print(f"Not enough money, you need {remaining_money:.2f} leva more.")
