town = input()
packages_type = input()
has_discount_card = input()
stay_time = int(input())
price = 0
total_price = 0

if (town == "Bansko" or town == "Borovets") and stay_time >= 1:
    if packages_type == "withEquipment":
        price = 100
    elif packages_type == "noEquipment":
        price = 80
    else:
        print("Invalid input!")
elif (town == "Varna" or town == "Burgas") and stay_time >= 1:
    if packages_type == "withBreakfast":
        price = 130
    elif packages_type == "noBreakfast":
        price = 100
    else:
        print("Invalid input!")
else:
    if stay_time < 1:
        print("Days must be positive number!")
    else:
        print("Invalid input!")

if has_discount_card == "yes":
    if town == "Bansko" or town == "Borovets":
        if packages_type == "withEquipment":
            price *= 0.9
        elif packages_type == "noEquipment":
            price *= 0.95
    elif town == "Varna" or town == "Burgas":
        if packages_type == "withBreakfast":
            price *= 0.88
        elif packages_type == "noBreakfast":
            price *= 0.93

total_price = price * stay_time

if stay_time > 7:
    total_price -= price

if (town == "Bansko" or town == "Borovets" or town == "Varna" or town == "Burgas") and stay_time >= 1 and \
        (packages_type == "withEquipment" or packages_type == "noEquipment" or packages_type == "withBreakfast"
         or packages_type == "noBreakfast"):
    print(f"The price is {total_price:.2f}lv! Have a nice time!")
