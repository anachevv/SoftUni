budget = float(input())
graphic_card_amount = int(input())
processor_amount = int(input())
memory_amount = int(input())

graphic_card = 250 * graphic_card_amount
processor = 0.35 * graphic_card * processor_amount
memory = 0.1 * graphic_card * memory_amount

total_price = graphic_card + processor + memory

if graphic_card_amount > processor_amount:
    total_price -= 0.15 * total_price
else:
    total_price += 0

remaining_money = abs(budget - total_price)

if budget >= total_price:
    print(f"You have {remaining_money:.2f} leva left!")
else:
    print(f"Not enough money! You need {remaining_money:.2f} leva more!")
