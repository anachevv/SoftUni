price_of_bags_above_20_kgs = float(input())
bags_weight = float(input())
days_to_the_travel = int(input())
bags_amount = int(input())

price = 0

if bags_weight < 10:
    price = 0.2 * price_of_bags_above_20_kgs
elif 10 <= bags_weight <= 20:
    price = 0.5 * price_of_bags_above_20_kgs
elif bags_weight > 20:
    price = price_of_bags_above_20_kgs

if days_to_the_travel > 30:
    price += 0.1 * price
elif 7 <= days_to_the_travel <= 30:
    price += 0.15 * price
elif days_to_the_travel < 7:
    price += 0.4 * price

total_price = price * bags_amount

print(f"The total price of bags is: {total_price:.2f} lv.")
