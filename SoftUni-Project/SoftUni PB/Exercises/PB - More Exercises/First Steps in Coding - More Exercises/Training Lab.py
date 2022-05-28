import math

# Variables
length = float(input()) * 100
width = float(input()) * 100 - 100

# seat - 70 x 120 cm
# corridor - 100 cm width
# entry door - 160 cm opening
# 1 seat less because of the entry door
# department - 160 x 120 cm
# 2 seats less because of the department

# limit: 3 <= w <= l <= 100

seats = math.floor(length / 120) * math.floor(width / 70) - 3
print(seats)
