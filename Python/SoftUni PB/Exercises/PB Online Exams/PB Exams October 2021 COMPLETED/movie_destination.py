budget = float(input())
destination = input()
season = input()
days = int(input())

price = 0

if season == "Winter":
    if destination == "Dubai":
        price = 45000
    elif destination == "Sofia":
        price = 17000
    elif destination == "London":
        price = 24000
elif season == "Summer":
    if destination == "Dubai":
        price = 40000
    elif destination == "Sofia":
        price = 12500
    elif destination == "London":
        price = 20250

if destination == "Dubai":
    price *= 0.7
elif destination == "Sofia":
    price *= 1.25

price *= days

if budget >= price:
    remaining_money = budget - price
    print(f"The budget for the movie is enough! We have {remaining_money:.2f} leva left!")
else:
    remaining_money = price - budget
    print(f"The director needs {remaining_money:.2f} leva more!")
