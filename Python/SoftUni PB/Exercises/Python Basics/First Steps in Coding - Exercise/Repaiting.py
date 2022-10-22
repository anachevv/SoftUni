protective_nylon = 1.5
paint = 14.5
paint_thinner = 5
nylon_quantity = int(input()) + 2
paint_quantity = int(input())
thinner_quantity = int(input())
time = int(input())
price = (nylon_quantity * 1.5) + ((paint_quantity + (10/100 * paint_quantity)) * 14.5) + 0.4 + (thinner_quantity * 5)
workers_money = (30/100 * price) * time
total = price + workers_money
print(total)
