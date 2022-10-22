months = int(input())

total_electricity_bill = 0
water_bill = 0
internet_bill = 0
other_bill = 0
total_bill = 0

for x in range(months):
    electricity_bill = float(input())

    total_electricity_bill += electricity_bill
    water_bill += 20
    internet_bill += 15
    other_bill += electricity_bill + 20 + 15 + 20 / 100 * (electricity_bill + 20 + 15)
total_bill += total_electricity_bill + water_bill + internet_bill + other_bill
average_bill = total_bill / months

print(f"Electricity: {total_electricity_bill:.2f} lv")
print(f"Water: {water_bill:.2f} lv")
print(f"Internet: {internet_bill:.2f} lv")
print(f"Other: {other_bill:.2f} lv")
print(f"Average: {average_bill:.2f} lv")
