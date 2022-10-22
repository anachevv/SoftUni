import math

tennis_racket_price = float(input())
tennis_racket_amount = int(input())
sneakers = int(input())

sneakers_price = (1/6 * tennis_racket_price) * sneakers
total_tennis_racket_price = tennis_racket_price * tennis_racket_amount
another_equipment = 20/100 * (sneakers_price + total_tennis_racket_price)

total_price = sneakers_price + total_tennis_racket_price + another_equipment

print(f"Price to be paid by Djokovic {math.floor(1/8 * total_price)}")
print(f"Price to be paid by sponsors {math.ceil(7/8 * total_price)}")
