joinery_quantity = int(input())
joinery_type = input()
receiving_way = input()

price = 0

if joinery_quantity < 10:
    print("Invalid order")
    exit()

if joinery_type == "90X130":
    price = 110 * joinery_quantity
    if 60 > joinery_quantity > 30:
        price *= 0.95
    elif joinery_quantity > 60:
        price *= 0.92
elif joinery_type == "100X150":
    price = 140 * joinery_quantity
    if 80 > joinery_quantity > 40:
        price *= 0.94
    elif joinery_quantity > 80:
        price *= 0.9
elif joinery_type == "130X180":
    price = 190 * joinery_quantity
    if 50 > joinery_quantity > 20:
        price *= 0.93
    elif joinery_quantity > 50:
        price *= 0.88
elif joinery_type == "200X300":
    price = 250 * joinery_quantity
    if 50 > joinery_quantity > 25:
        price *= 0.91
    elif joinery_quantity > 50:
        price *= 0.86

if receiving_way == "With delivery":
    price += 60
if joinery_quantity > 99:
    price *= 0.96

print(f"{price:.2f} BGN")
