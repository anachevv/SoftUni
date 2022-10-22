sequence_of_items = input().split()
products_to_buy = input().split()

dct = {}

for i in range(0, len(sequence_of_items), 2):
    key = sequence_of_items[i]
    value = sequence_of_items[i + 1]
    dct[key] = int(value)

for product in products_to_buy:
    if product in dct:
        print(f"We have {dct[product]} of {product} left")
    else:
        print(f"Sorry, we don't have {product}")
