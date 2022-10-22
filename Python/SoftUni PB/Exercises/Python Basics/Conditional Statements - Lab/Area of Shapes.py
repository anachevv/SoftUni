from math import pi

print("square, rectangle, circle, triangle")

user_input = input()
area = 0.0
a = float(input())

if user_input == "square":
    area = a * a
elif user_input == "rectangle":
    b = float(input())
    area = a * b
elif user_input == "circle":
    area = pi * (a * a)
elif user_input == "triangle":
    h_a = float(input())
    area = (a * h_a) / 2

print("%.3f" % area)
