eggs = int(input())
red = 0
orange = 0
blue = 0
green = 0
colour_list = []

for x in range(0, eggs):
    egg_colour = input()

    if egg_colour == "red":
        red += 1
        colour_list.append(red)
    if egg_colour == "orange":
        orange += 1
        colour_list.append(orange)
    if egg_colour == "blue":
        blue += 1
        colour_list.append(blue)
    if egg_colour == "green":
        green += 1
        colour_list.append(green)

max_eggs = max(colour_list)
max_colour = ""

if red > green and red > blue and red > orange:
    max_colour = "red"
elif green > red and green > blue and green > orange:
    max_colour = "green"
elif blue > red and blue > green and blue > orange:
    max_colour = "blue"
elif orange > blue and orange > red and orange > green:
    max_colour = "orange"

print(f"Red eggs: {red}\nOrange eggs: {orange}\nBlue eggs: {blue}\nGreen eggs: {green}"
      f"\nMax eggs: {max_eggs} -> {max_colour}")
