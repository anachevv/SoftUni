wanted_money = int(input())
command = input()

price = 0

while command != "closed":
    current_service = command

    if current_service == "haircut":
        age_type = input()

        if age_type == "mens":
            price += 15
        elif age_type == "ladies":
            price += 20
        elif age_type == "kids":
            price += 10

    elif current_service == "color":
        color_type = input()

        if color_type == "touch up":
            price += 20
        elif color_type == "full color":
            price += 30

    if price >= wanted_money:
        print("You have reached your target for the day!")
        print(f"Earned money: {price}lv.")
        break

    command = input()

if price < wanted_money:
    needed_money = wanted_money - price
    print(f"Target not reached! You need {needed_money}lv. more.")
    print(f"Earned money: {price}lv.")
