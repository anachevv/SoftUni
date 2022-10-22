stay_time = int(input()) - 1
room_type = input()
evaluation = input()
price = 0

if room_type == "room for one person":
    price = 18 * stay_time

elif room_type == "apartment":
    price = 25 * stay_time
    if stay_time < 10:
        price *= 0.7
    elif 10 <= stay_time <= 15:
        price *= 0.65
    else:
        price *= 0.5

elif room_type == "president apartment":
    price = 35 * stay_time
    if stay_time < 10:
        price *= 0.9
    elif 10 <= stay_time <= 15:
        price *= 0.85
    else:
        price *= 0.8

if evaluation == "positive":
    price += 0.25 * price
elif evaluation == "negative":
    price -= 0.1 * price

print(f"{price:.2f}")
