user_input = float(input())

if 26.00 <= user_input <= 35.00:
    print("Hot")
elif 20.1 <= user_input <= 25.9:
    print("Warm")
elif 15.00 <= user_input <= 20.00:
    print("Mild")
elif 12.00 <= user_input <= 14.9:
    print("Cool")
elif 5.00 <= user_input <= 11.9:
    print("Cold")
else:
    print("unknown")
