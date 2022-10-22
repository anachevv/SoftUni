text = input()
total_balance = 0

while text != "NoMoreMoney":
    payment = float(text)

    if payment < 0:
        print("Invalid operation!")
        break

    total_balance += payment
    print(f"Increase: {payment:.2f}")
    text = input()

print(f"Total: {total_balance:.2f}")
