cinema_capacity = int(input())
people = input()

people_entering = 0
price = 0
ticket_price = 5

while people != "Movie time!":

    people_entering += int(people)

    if cinema_capacity < people_entering:
        print("The cinema is full.")
        break

    price += int(people) * ticket_price

    if int(people) % 3 == 0:
        price -= ticket_price

    people = input()

if people == "Movie time!":
    print(f"There are {cinema_capacity - people_entering} seats left in the cinema.")

print(f"Cinema income - {price} lv.")
