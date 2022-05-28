# Variables
price_kilo_veg = float(input())
price_kilo_fruits = float(input())
veg_kilos = int(input())
fruits_kilos = int(input())

income = ((price_kilo_veg * veg_kilos) + (price_kilo_fruits * fruits_kilos)) / 1.94
print(float(income))