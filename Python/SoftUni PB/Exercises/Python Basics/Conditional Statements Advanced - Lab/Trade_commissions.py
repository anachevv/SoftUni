city = input()
sells_amount = float(input())

if city == "Sofia":
    if 0 <= sells_amount <= 500:
        commission = 0.05 * sells_amount
        print(f"{commission:.2f}")
    elif 500 < sells_amount <= 1000:
        commission = 0.07 * sells_amount
        print(f"{commission:.2f}")
    elif 1000 < sells_amount <= 10000:
        commission = 0.08 * sells_amount
        print(f"{commission:.2f}")
    elif sells_amount > 10000:
        commission = 0.12 * sells_amount
        print(f"{commission:.2f}")
    else:
        print("error")
elif city == "Varna":
    if 0 <= sells_amount <= 500:
        commission = 0.045 * sells_amount
        print(f"{commission:.2f}")
    elif 500 < sells_amount <= 1000:
        commission = 0.075 * sells_amount
        print(f"{commission:.2f}")
    elif 1000 < sells_amount <= 10000:
        commission = 0.1 * sells_amount
        print(f"{commission:.2f}")
    elif sells_amount > 10000:
        commission = 0.13 * sells_amount
        print(f"{commission:.2f}")
    else:
        print("error")
elif city == "Plovdiv":
    if 0 <= sells_amount <= 500:
        commission = 0.055 * sells_amount
        print(f"{commission:.2f}")
    elif 500 < sells_amount <= 1000:
        commission = 0.08 * sells_amount
        print(f"{commission:.2f}")
    elif 1000 < sells_amount <= 10000:
        commission = 0.12 * sells_amount
        print(f"{commission:.2f}")
    elif sells_amount > 10000:
        commission = 0.145 * sells_amount
        print(f"{commission:.2f}")
    else:
        print("error")
else:
    print("error")
