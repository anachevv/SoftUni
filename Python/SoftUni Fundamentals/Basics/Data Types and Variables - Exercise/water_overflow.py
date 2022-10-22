max_capacity = 255
current_volume = 0
n_lines = int(input())

for current_liters in range(n_lines):
    pouring = int(input())
    current_volume += pouring

    if current_volume > max_capacity:
        print('Insufficient capacity!')
        current_volume -= pouring
        continue

print(current_volume)
