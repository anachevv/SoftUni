projection = input()
rows = int(input())
columns = int(input())

full_cinema_hall = rows * columns
price = 0
income = 0

if projection == "Premiere":
    price = 12.00
elif projection == "Normal":
    price = 7.50
elif projection == "Discount":
    price = 5.00

income = price * full_cinema_hall

print(f"{income:.2f} leva")
