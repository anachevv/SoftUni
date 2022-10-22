weight = float(input())
service_type = input()
distance = int(input())

transport_price = 0
surcharge_per_kg = 0

if service_type == "standard":
    if weight < 1:
        transport_price = 0.03 * distance
    elif 1 <= weight < 10:
        transport_price = 0.05 * distance
    elif 10 <= weight < 40:
        transport_price = 0.1 * distance
    elif 40 <= weight < 90:
        transport_price = 0.15 * distance
    elif 90 <= weight < 150:
        transport_price = 0.2 * distance
elif service_type == "express":
    if weight < 1:
        transport_price = distance * 0.03
        surcharge_per_kg = 0.8 * 0.03
    elif 1 <= weight < 10:
        transport_price = 0.05 * distance
        surcharge_per_kg = 0.4 * 0.05
    elif 10 <= weight < 40:
        transport_price = 0.1 * distance
        surcharge_per_kg = 0.05 * 0.1
    elif 40 <= weight < 90:
        transport_price = 0.15 * distance
        surcharge_per_kg = 0.02 * 0.15
    elif 90 <= weight < 150:
        transport_price = 0.2 * distance
        surcharge_per_kg = 0.01 * 0.2

surcharge_per_km = weight * surcharge_per_kg
total_surcharge = distance * surcharge_per_km
total_price = transport_price + total_surcharge

print(f"The delivery of your shipment with weight of {weight:.3f} kg. would cost {total_price:.2f} lv.")
