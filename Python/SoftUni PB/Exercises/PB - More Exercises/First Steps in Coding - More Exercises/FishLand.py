price_mackerel = float(input())
price_sprat = float(input())

kg_bonito = float(input())
kg_horse_mackerel = float(input())
kg_mussels = int(input())

price_bonito = ((0.6 * price_mackerel) + price_mackerel) * kg_bonito
price_horse_mackerel = ((0.8 * price_sprat) + price_sprat) * kg_horse_mackerel
price_mussels = 7.5 * kg_mussels

total_price = price_bonito + price_horse_mackerel + price_mussels

print(f"{total_price:.2f}")
