fruit = input()
day = input()
amount = float(input())

if day == "Monday" or day == "Tuesday" or day == "Wednesday" or \
    day == "Thursday" or day == "Friday":
    if fruit == "banana":
        price = 2.5
        total = price * amount
        print(f"{total:.2f}")
    elif fruit == "apple":
        price = 1.2
        total = price * amount
        print(f"{total:.2f}")
    elif fruit == "orange":
        price = 0.85
        total = price * amount
        print(f"{total:.2f}")
    elif fruit == "grapefruit":
        price = 1.45
        total = price * amount
        print(f"{total:.2f}")
    elif fruit == "kiwi":
        price = 2.7
        total = price * amount
        print(f"{total:.2f}")
    elif fruit == "pineapple":
        price = 5.5
        total = price * amount
        print(f"{total:.2f}")
    elif fruit == "grapes":
        price = 3.85
        total = price * amount
        print(f"{total:.2f}")
    else:
        print("error")

elif day == "Saturday" or day == "Sunday":
    if fruit == "banana":
        price = 2.7
        total = price * amount
        print(f"{total:.2f}")
    elif fruit == "apple":
        price = 1.25
        total = price * amount
        print(f"{total:.2f}")
    elif fruit == "orange":
        price = 0.9
        total = price * amount
        print(f"{total:.2f}")
    elif fruit == "grapefruit":
        price = 1.60
        total = price * amount
        print(f"{total:.2f}")
    elif fruit == "kiwi":
        price = 3
        total = price * amount
        print(f"{total:.2f}")
    elif fruit == "pineapple":
        price = 5.6
        total = price * amount
        print(f"{total:.2f}")
    elif fruit == "grapes":
        price = 4.2
        total = price * amount
        print(f"{total:.2f}")
    else:
        print("error")
else:
    print("error")
