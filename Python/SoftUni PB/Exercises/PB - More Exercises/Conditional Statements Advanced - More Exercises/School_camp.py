season = input()
group = input()
students = int(input())
overnights = int(input())
vacation = ""
price = 0
sport = ""

if season == "Winter":
    if group == "girls":
        sport = "Gymnastics"
    elif group == "boys":
        sport = "Judo"
    elif group == "mixed":
        sport = "Ski"

    if group == "girls" or group == "boys":
        price = students * 9.6 * overnights
    elif group == "mixed":
        price = students * 10 * overnights

elif season == "Spring":
    if group == "girls":
        sport = "Athletics"
    elif group == "boys":
        sport = "Tennis"
    elif group == "mixed":
        sport = "Cycling"

    if group == "girls" or group == "boys":
        price = students * 7.2 * overnights
    elif group == "mixed":
        price = students * 9.5 * overnights

elif season == "Summer":
    if group == "girls":
        sport = "Volleyball"
    elif group == "boys":
        sport = "Football"
    elif group == "mixed":
        sport = "Swimming"

    if group == "girls" or group == "boys":
        price = students * 15 * overnights
    elif group == "mixed":
        price = students * 20 * overnights

if students >= 50:
    price *= 0.5
elif 20 <= students < 50:
    price *= 0.85
elif 10 <= students < 20:
    price *= 0.95

print(f"{sport} {price:.2f} lv.")
