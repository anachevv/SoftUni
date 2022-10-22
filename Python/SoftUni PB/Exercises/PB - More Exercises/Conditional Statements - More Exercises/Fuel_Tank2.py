gasoline_price = 2.22
diesel_price = 2.33
gas_price = 0.93
price = 0

type_fuel = input()
fuel_liters = float(input())
has_discount_card = input()

if type_fuel == "Gas":
    price = gas_price * fuel_liters
elif type_fuel == "Gasoline":
    price = gasoline_price * fuel_liters
elif type_fuel == "Diesel":
    price = diesel_price * fuel_liters

if has_discount_card == "Yes":
    if type_fuel == "Gas":
        discount = 0.08 * fuel_liters
        price -= discount
    elif type_fuel == "Gasoline":
        discount = 0.18 * fuel_liters
        price -= discount
    elif type_fuel == "Diesel":
        discount = 0.12 * fuel_liters
        price -= discount

if 20 <= fuel_liters <= 25:
    price *= 0.92
elif fuel_liters > 25:
    price *= 0.90


print(f"{price:.2f} lv.")
