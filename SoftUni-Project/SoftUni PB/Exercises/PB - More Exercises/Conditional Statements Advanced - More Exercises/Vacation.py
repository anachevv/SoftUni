budget = float(input())
season = input()
accommodation = ""
location = ""
price = 0

if budget <= 1000:
    accommodation = "Camp"
    if season == "Summer":
        location = "Alaska"
        price = 0.65 * budget
    elif season == "Winter":
        location = "Morocco"
        price = 0.45 * budget
elif 1000 < budget <= 3000:
    accommodation = "Hut"
    if season == "Summer":
        location = "Alaska"
        price = 0.8 * budget
    elif season == "Winter":
        location = "Morocco"
        price = 0.6 * budget
elif budget > 3000:
    accommodation = "Hotel"
    price = 0.9 * budget
    if season == "Summer":
        location = "Alaska"
    elif season == "Winter":
        location = "Morocco"

print(f"{location} - {accommodation} - {price:.2f}")
