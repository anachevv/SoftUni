n_of_loads = int(input())
price = 0
total_weight = 0
weight = 0

minibus = 0
truck = 0
train = 0

for x in range(n_of_loads):
    weight = int(input())
    if weight <= 3:
        price += 200 * weight
        minibus += weight
        total_weight += weight
    elif weight <= 11:
        price += 175 * weight
        truck += weight
        total_weight += weight
    else:
        price += 120 * weight
        train += weight
        total_weight += weight

print(f"{price / (minibus + truck + train):.2f}")
print(f"{minibus / total_weight * 100:.2f}%\n{truck / total_weight * 100:.2f}%\n{train / total_weight * 100:.2f}%")
