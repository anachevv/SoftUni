month = input()
overnight_stays = int(input())
studio_price = 0
apartment_price = 0

if month == "May" or month == "October":
    studio_price = 50 * overnight_stays
    apartment_price = 65 * overnight_stays
    if overnight_stays > 14:
        studio_price *= 0.7
    elif overnight_stays > 7:
        studio_price *= 0.95


elif month == "June" or month == "September":
    studio_price = 75.2 * overnight_stays
    apartment_price = 68.70 * overnight_stays
    if overnight_stays > 14:
        studio_price *= 0.8
elif month == "July" or month == "August":
    studio_price = 76 * overnight_stays
    apartment_price = 77 * overnight_stays

if overnight_stays > 14:
    apartment_price *= 0.9

print(f"Apartment: {apartment_price:.2f} lv.")
print(f"Studio: {studio_price:.2f} lv.")
