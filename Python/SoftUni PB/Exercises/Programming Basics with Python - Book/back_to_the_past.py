heritage = float(input())
year = int(input())
age = 18

for x in range(1800, year + 1):
    if x % 2 == 0:
        heritage -= 12000
    else:
        heritage -= (12000 + 50 * age)
    age += 1

if heritage >= 0:
    print(f"Yes! He will live a carefree life and will have {heritage:.2f} dollars left.")
else:
    print(f"He will need {abs(heritage):.2f} dollars to survive.")
