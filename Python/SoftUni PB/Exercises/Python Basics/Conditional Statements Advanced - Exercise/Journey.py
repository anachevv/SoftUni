budget = float(input())
season = input()
price = 0
vacation = ""

if budget <= 100:
    if season == "summer":
        price = 0.3 * budget
        vacation = "Camp"
        print("Somewhere in Bulgaria")
    elif season == "winter":
        price = 0.7 * budget
        vacation = "Hotel"
        print("Somewhere in Bulgaria")
elif budget <= 1000:
    if season == "summer":
        price = 0.4 * budget
        vacation = "Camp"
        print("Somewhere in Balkans")
    elif season == "winter":
        price = 0.8 * budget
        vacation = "Hotel"
        print("Somewhere in Balkans")
elif budget > 1000:
    price = 0.9 * budget
    vacation = "Hotel"
    print("Somewhere in Europe")

print(f"{vacation} - {price:.2f}")
