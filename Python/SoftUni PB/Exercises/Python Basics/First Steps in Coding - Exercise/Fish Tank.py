length = int(input())
width = int(input())
height = int(input())
percent = float(input())
water_quantity = ((length * width * height) / 1000) * (1 - percent/100)

print(water_quantity)
