budget = float(input())
category = input()
fans_number = int(input())
ticket_price = 0
transport_price = 0

if category == "VIP":
    ticket_price = 499.99 * fans_number
elif category == "Normal":
    ticket_price = 249.99 * fans_number

if 1 <= fans_number <= 4:
    transport_price = 0.75 * budget
elif 5 <= fans_number <= 9:
    transport_price = 0.6 * budget
elif 10 <= fans_number <= 24:
    transport_price = 0.5 * budget
elif 25 <= fans_number <= 49:
    transport_price = 0.4 * budget
elif fans_number >= 50:
    transport_price = 0.25 * budget

total_price = ticket_price + transport_price

if budget >= total_price:
    print(f"Yes! You have {(budget - total_price):.2f} leva left.")
else:
    print(f"Not enough money! You need {(total_price - budget):.2f} leva.")
