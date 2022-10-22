paper = int(input())
fabric = int(input())
glue_liters = float(input())
discount_percent = int(input()) / 100

paper_price = paper * 5.8
fabric_price = fabric * 7.2
glue_price = glue_liters * 1.2
price = paper_price + fabric_price + glue_price
total_price = price - (discount_percent * price)

print(f"{total_price:.3f}")
