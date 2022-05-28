wanted_income = float(input())
earned_money = 0

while earned_money < wanted_income:

    cocktail_name = input()
    cocktail_price = 0

    if cocktail_name == "Party!":
        print(f"We need {wanted_income - earned_money:.2f} leva more.")
        break

    cocktails_amount = int(input())
    cocktail_price += len(cocktail_name) * cocktails_amount

    if cocktail_price % 2 != 0:
        cocktail_price *= 0.75

    earned_money += cocktail_price

if earned_money >= wanted_income:
    print("Target acquired.")

print(f"Club income - {earned_money:.2f} leva.")
