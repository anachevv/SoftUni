projection = input()
movie_packet = input()
tickets = int(input())

price = 0

if movie_packet == "Drink":
    if projection == "John Wick":
        price = 12
    elif projection == "Star Wars":
        price = 18
    elif projection == "Jumanji":
        price = 9
elif movie_packet == "Popcorn":
    if projection == "John Wick":
        price = 15
    elif projection == "Star Wars":
        price = 25
    elif projection == "Jumanji":
        price = 11
elif movie_packet == "Menu":
    if projection == "John Wick":
        price = 19
    elif projection == "Star Wars":
        price = 30
    elif projection == "Jumanji":
        price = 14

if projection == "Star Wars" and tickets >= 4:
    price *= 0.7
elif projection == "Jumanji" and tickets == 2:
    price *= 0.85

total_price = price * tickets

print(f"Your bill is {total_price:.2f} leva.")
