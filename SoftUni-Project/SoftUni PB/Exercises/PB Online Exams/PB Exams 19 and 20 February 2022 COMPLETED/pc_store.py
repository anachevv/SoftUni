processor_price = float(input()) * 1.57
graphic_card_price = float(input()) * 1.57
memory_price = float(input()) * 1.57
memory_quantity = int(input())
discount_percent = float(input())

processor_price -= discount_percent * processor_price
graphic_card_price -= discount_percent * graphic_card_price
memory_price *= memory_quantity

total_price = processor_price + graphic_card_price + memory_price

print(f"Money needed - {total_price:.2f} leva.")
