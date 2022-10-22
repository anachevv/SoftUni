import math

people = int(input())
entry_price = float(input())
price_chaise_long = float(input())
price_umbrella = float(input())

total_price = people * entry_price + (math.ceil(0.75 * people) * price_chaise_long) + \
              (math.ceil(people / 2) * price_umbrella)

print(f"{total_price:.2f} lv.")
