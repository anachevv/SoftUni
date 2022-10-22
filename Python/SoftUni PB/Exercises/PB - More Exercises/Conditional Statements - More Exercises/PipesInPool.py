volume = int(input())
p1_per_hour = int(input())
p2_per_hour = int(input())
time = float(input())

p1_liters = p1_per_hour * time
p2_liters = p2_per_hour * time
filled_volume = (p1_per_hour + p2_per_hour) * time

if filled_volume > volume:
    excess_liters = filled_volume - volume
    print(f"For {time:.2f} hours the pool overflows with "
          f"{excess_liters:.2f} liters.")
else:
    print(f"The pool is {(filled_volume / volume * 100):.2f}% full. Pipe 1: "
          f"{(p1_liters / filled_volume * 100):.2f}%. "
          f"Pipe 2: {(p2_liters / filled_volume * 100):.2f}%.")
