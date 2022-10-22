products = {}

command = input()
while command != 'statistics':
    if command == 'statistics':
        break
    command = command.split(': ')
    product = command[0]
    quantity = int(command[1])
    if product not in products:
        products[product] = 0
    products[product] += quantity

    command = input()

print("Products in stock:")

for product, quantity in products.items():
    print(f"- {product}: {quantity}")

total_products = len(products.keys())
total_sum = sum(products.values())

print(f"Total Products: {total_products}")
print(f"Total Quantity: {total_sum}")
