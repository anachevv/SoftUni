n_days = int(input())
total_brandy_quantity = 0
total_degrees = 0

for quantity_and_degrees in range(n_days):
    brandy_quantity = float(input())
    degrees_of_brandy = float(input())

    total_brandy_quantity += brandy_quantity
    total_degrees += brandy_quantity * degrees_of_brandy

average_degrees = total_degrees / total_brandy_quantity

print(f"Liter: {total_brandy_quantity:.2f}")
print(f"Degrees: {average_degrees:.2f}")
if average_degrees < 38:
    print("Not good, you should baking!")
elif 38 <= average_degrees <= 42:
    print("Super")
elif average_degrees > 42:
    print("Dilution with distilled water!")
