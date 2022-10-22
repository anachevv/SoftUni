user_input_product = input()
user_input_city = input()
user_input_amount = float(input())
price = 0

if user_input_city == "Sofia":
    if user_input_product == "coffee":
        price = 0.5
    elif user_input_product == "water":
        price = 0.8
    elif user_input_product == "beer":
        price = 1.2
    elif user_input_product == "sweets":
        price = 1.45
    elif user_input_product == "peanuts":
        price = 1.6
elif user_input_city == "Plovdiv":
    if user_input_product == "coffee":
        price = 0.4
    elif user_input_product == "water":
        price = 0.7
    elif user_input_product == "beer":
        price = 1.15
    elif user_input_product == "sweets":
        price = 1.3
    elif user_input_product == "peanuts":
        price = 1.5
elif user_input_city == "Varna":
    if user_input_product == "coffee":
        price = 0.45
    elif user_input_product == "water":
        price = 0.7
    elif user_input_product == "beer":
        price = 1.10
    elif user_input_product == "sweets":
        price = 1.35
    elif user_input_product == "peanuts":
        price = 1.55

total_price = price * user_input_amount

print(total_price)
