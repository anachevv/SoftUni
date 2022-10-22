from collections import deque

chocolates = [int(x) for x in input().split(', ')]
milk_cups = deque([int(x) for x in input().split(', ')])
milkshakes = 0
while chocolates and milk_cups and milkshakes < 5:
    chocolate = chocolates.pop()
    milk = milk_cups.popleft()

    if chocolate <= 0 and milk <= 0:
        continue
    if chocolate <= 0:
        milk_cups.appendleft(milk)
        continue
    if milk <= 0:
        chocolates.append(chocolate)
        continue
    if chocolate == milk:
        milkshakes += 1
    else:
        chocolates.append(chocolate - 5)
        milk_cups.append(milk)
print("Great! You made all the chocolate milkshakes needed!") if milkshakes == 5 else print("Not enough milkshakes.")
print(f"Chocolate: {', '.join(str(x) for x in chocolates)}") if chocolates else print("Chocolate: empty")
print(f"Milk: {', '.join(str(x) for x in milk_cups)}") if milk_cups else print("Milk: empty")
