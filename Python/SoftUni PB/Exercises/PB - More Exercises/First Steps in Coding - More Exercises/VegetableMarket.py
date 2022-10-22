price_vegetables = float(input())
price_fruits = float(input())
kg_vegetables = int(input())
kg_fruits = int(input())

total_price_vegetables = price_vegetables * kg_vegetables
total_price_fruits = price_fruits * kg_fruits

total = (total_price_vegetables + total_price_fruits) / 1.94

print(f"{total:.2f}")
