user_input = input()

working_day = {"Monday", "Tuesday", "Wednesday", "Thursday", "Friday"}
weekend = {"Saturday", "Sunday"}

if user_input in working_day:
    print("Working day")
elif user_input in weekend:
    print("Weekend")
else:
    print("Error")
