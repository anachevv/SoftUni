food_and_quantity = input().split()
dct = {}

for x in range(0, len(food_and_quantity), 2):
    key = food_and_quantity[x]
    value = food_and_quantity[x + 1]
    dct[key] = int(value)

print(dct)
