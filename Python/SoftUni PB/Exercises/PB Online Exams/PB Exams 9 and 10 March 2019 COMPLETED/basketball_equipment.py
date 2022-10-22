annual_tax = int(input())

basketball_sneakers = 0.6 * annual_tax
basketball_outfit = 0.8 * basketball_sneakers
basketball_ball = 1/4 * basketball_outfit
basketball_accessories = 1/5 * basketball_ball

total_price = basketball_sneakers + basketball_outfit + basketball_ball + basketball_accessories + annual_tax

print(f"{total_price:.2f}")
