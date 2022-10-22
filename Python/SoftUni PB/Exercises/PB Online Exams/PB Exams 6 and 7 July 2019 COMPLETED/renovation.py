height_wall = int(input())
width_wall = int(input())
percent_unpainted_wall = int(input())

total_liters = width_wall * height_wall * 4
total_liters *= 1 - percent_unpainted_wall / 100


while True:
    paint = input()

    if paint == "Tired!":
        print(f"{total_liters:.0f} quadratic m left.")
        break

    total_liters -= int(paint)

    if total_liters < 0:
        left = abs(total_liters)
        print(f"All walls are painted and you have {left:.0f} l paint left!")
        break

    elif total_liters == 0:
        print("All walls are painted! Great job, Pesho!")
        break
