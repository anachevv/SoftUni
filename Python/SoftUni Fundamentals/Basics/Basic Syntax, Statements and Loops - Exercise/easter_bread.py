budget = float(input())
flour_price = float(input())

colored_eggs = 0
egg_pack_price = 0.75 * flour_price
milk_price = 1.25 * flour_price / 4
loaf_price = egg_pack_price + milk_price + flour_price
breads_count = 0

while budget > 0:

    if budget < loaf_price:
        print(f'You made {breads_count} loaves of Easter bread! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.')
        break
    budget -= loaf_price
    colored_eggs += 3
    breads_count += 1

    if breads_count % 3 == 0:
        colored_eggs -= (breads_count - 2)
