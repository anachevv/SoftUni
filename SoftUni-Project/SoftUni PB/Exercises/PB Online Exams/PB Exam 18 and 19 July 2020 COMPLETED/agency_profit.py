airline_name = input()
tickets_for_adults = int(input())
tickets_for_kids = int(input())
ticket_price_for_adults = float(input())
service_price = float(input())

ticket_price_for_kids = 0.3 * ticket_price_for_adults

total_price_for_kids = tickets_for_kids * (ticket_price_for_kids + service_price)
total_price_for_adults = tickets_for_adults * (ticket_price_for_adults + service_price)

price = total_price_for_adults + total_price_for_kids
total_profit = 0.2 * price

print(f"The profit of your agency from {airline_name} tickets is {total_profit:.2f} lv.")
