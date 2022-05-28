needed_money = float(input())
money_in_pocket = float(input())
days_counter = 0
spending_counter = 0
max_spend_days = False

while money_in_pocket < needed_money:
    action = input()
    current_money = float(input())
    days_counter += 1

    if action == "spend":
        money_in_pocket -= current_money
        spending_counter += 1
        if money_in_pocket < 0:
            money_in_pocket = 0
        if spending_counter == 5:
            max_spend_days = True
            break

    elif action == "save":
        spending_counter = 0
        money_in_pocket += current_money
        if current_money >= needed_money:
            break

if max_spend_days:
    print("You can't save the money.")
    print(days_counter)
else:
    print(f"You saved the money for {days_counter} days.")
