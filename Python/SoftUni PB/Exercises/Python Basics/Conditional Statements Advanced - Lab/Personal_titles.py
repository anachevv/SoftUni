user_input_age = float(input())
user_input_gender = input()

if user_input_gender == "m":
    if user_input_age >= 16:
        print("Mr.")
    else:
        print("Master")
elif user_input_gender == "f":
    if user_input_age >= 16:
        print("Ms.")
    else:
        print("Miss")
