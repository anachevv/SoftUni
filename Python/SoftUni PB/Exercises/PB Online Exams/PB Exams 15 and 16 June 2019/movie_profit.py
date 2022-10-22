movie_name = input()
days = int(input())
tickets = int(input())
ticket_price = float(input())
percent_for_the_cinema = int(input()) / 100

price = days * tickets * ticket_price
total_price = price - percent_for_the_cinema * price

print(f"The profit from the movie {movie_name} is {total_price:.2f} lv.")
