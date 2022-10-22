from math import pi

r = float(input())

perimeter = 2 * pi * r
area = pi * (pow(r, 2))

print(f"{area:.2f}")
print(f"{perimeter:.2f}")
