import math

x_vineyard_area = int(input())
y_grapes_kg_per_km2 = float(input())
z_necessary_wine_liters = int(input())
workers = int(input())

total_grapes = x_vineyard_area * y_grapes_kg_per_km2
produced_wine = 0.4 * total_grapes / 2.5

if produced_wine < z_necessary_wine_liters:
    missing_quantity = z_necessary_wine_liters - produced_wine
    print(f"It will be a tough winter! More {math.floor(missing_quantity)} "
          f"liters wine needed.")
elif produced_wine >= z_necessary_wine_liters:
    remaining_wine = produced_wine - z_necessary_wine_liters
    wine_per_worker = (produced_wine - z_necessary_wine_liters) / workers
    print(f"Good harvest this year! Total wine: {math.floor(produced_wine)} liters.")
    print(f"{math.ceil(remaining_wine)} liters left -> "
          f"{math.ceil(wine_per_worker)} liters per person.")

