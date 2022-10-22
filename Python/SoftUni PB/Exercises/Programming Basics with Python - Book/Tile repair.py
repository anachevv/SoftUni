a = int(input())
tile_width = float(input())
tile_length = float(input())
bench_width = int(input())
bench_length = int(input())

area = a * a - 2
tile = tile_width * tile_length
tiles_quantity = area / tile
time = tiles_quantity * 0.2

print(round(tiles_quantity, 2))
print(round(time, 2))
