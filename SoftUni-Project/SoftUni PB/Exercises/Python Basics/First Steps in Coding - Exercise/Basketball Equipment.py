annuel_fee = int(input())
shoes = annuel_fee - (40/100 * annuel_fee)
outfit = shoes - (20/100 * shoes)
ball = 1/4 * outfit
accessories = 1/5 * ball
total = annuel_fee + shoes + outfit + ball + accessories
print(total)