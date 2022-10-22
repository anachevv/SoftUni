import math

user_input_magnolias = int(input())
user_input_hyacinths = int(input())
user_input_roses = int(input())
user_input_cacti = int(input())
gift_price = float(input())

magnolias = user_input_magnolias * 3.25
hyacinths = user_input_hyacinths * 4
roses = user_input_roses * 3.5
cacti = user_input_cacti * 8

profit = magnolias + hyacinths + roses + cacti
taxes = 0.05 * profit
total_profit = profit - taxes

if total_profit >= gift_price:
    rest = math.floor(total_profit - gift_price)
    print(f"She is left with {rest} leva.")
elif total_profit < gift_price:
    rest = math.ceil(gift_price - total_profit)
    print(f"She will have to borrow {rest} leva.")
