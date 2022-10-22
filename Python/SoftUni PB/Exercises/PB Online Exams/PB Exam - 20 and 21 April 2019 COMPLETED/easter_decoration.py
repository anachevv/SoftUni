clients = int(input())
price = 0
count = 0
total_price = 0

for x in range(clients):
    purchase = input()

    while purchase != "Finish":
        count += 1
        if purchase == "basket":
            price += 1.5
        elif purchase == "wreath":
            price += 3.8
        elif purchase == "chocolate bunny":
            price += 7
        purchase = input()

    if count % 2 == 0:
        price *= 0.8

    print(f"You purchased {count} items for {price:.2f} leva.")

    total_price += price
    price = 0
    count = 0

average_price = total_price / clients

print(f"Average bill per client is: {average_price:.2f} leva.")
