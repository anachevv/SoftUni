easter_breads = int(input())
eggshells = int(input())
cookies = int(input())

easter_cakes_price = easter_breads * 3.2
eggs_price = eggshells * 4.35
paint_price = eggshells * 12 * 0.15
cookies_price = cookies * 5.4

total_price = easter_cakes_price + eggs_price + cookies_price + paint_price

print(f"{total_price:.2f}")
