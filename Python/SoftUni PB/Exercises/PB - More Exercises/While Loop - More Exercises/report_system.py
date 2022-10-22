needed_money = int(input())


money_cash = 0
money_card = 0
total_counter = 0
cash_money = 0
card_money = 0


while needed_money > 0:

    current_money = input()

    if current_money == "End":
        print("Failed to collect required money for charity.")
        break

    current_money = int(current_money)
    total_counter += 1

    if total_counter % 2 == 1 and current_money <= 100:
        cash_money += 1
        money_card += current_money
        needed_money -= current_money
        print("Product sold!")

    elif total_counter % 2 == 0 and current_money >= 10:
        card_money += 1
        money_cash += current_money
        needed_money -= current_money
        print("Product sold!")

    else:
        print("Error in transaction!")


if needed_money <= 0:
    print(f"Average CS: {money_card / cash_money:.2f}")
    print(f"Average CC: {money_cash / card_money:.2f}")
