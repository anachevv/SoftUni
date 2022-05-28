stage = input()
ticket_type = input()
tickets = int(input())
photo = input()
price = 0
free_photo = False

if stage == "Quarter final":
    if ticket_type == "Standard":
        price = 55.5 * tickets
    elif ticket_type == "Premium":
        price = 105.2 * tickets
    elif ticket_type == "VIP":
        price = 118.9 * tickets
elif stage == "Semi final":
    if ticket_type == "Standard":
        price = 75.88 * tickets
    elif ticket_type == "Premium":
        price = 125.22 * tickets
    elif ticket_type == "VIP":
        price = 300.4 * tickets
elif stage == "Final":
    if ticket_type == "Standard":
        price = 110.1 * tickets
    elif ticket_type == "Premium":
        price = 160.66 * tickets
    elif ticket_type == "VIP":
        price = 400 * tickets

if price > 4000:
    price *= 0.75
    free_photo = True

elif price > 2500:
    price *= 0.90

if not free_photo and photo == "Y":
    price += 40 * tickets

print(f"{price:.2f}")
