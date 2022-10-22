drink = input()
sugar = input()
drink_number = int(input())
price = 0
total_price = 0

if drink == "Espresso":
    if sugar == "Without":
        price = 0.9
    elif sugar == "Normal":
        price = 1
    elif sugar == "Extra":
        price = 1.2

elif drink == "Cappuccino":
    if sugar == "Without":
        price = 1
    elif sugar == "Normal":
        price = 1.2
    elif sugar == "Extra":
        price = 1.6

elif drink == "Tea":
    if sugar == "Without":
        price = 0.5
    elif sugar == "Normal":
        price = 0.6
    elif sugar == "Extra":
        price = 0.7

if sugar == "Without":
    price *= 0.65

if drink == "Espresso" and drink_number >= 5:
    price *= 0.75

total_price = price * drink_number

if total_price > 15:
    total_price *= 0.8

print(f"You bought {drink_number} cups of {drink} for {total_price:.2f} lv.")
