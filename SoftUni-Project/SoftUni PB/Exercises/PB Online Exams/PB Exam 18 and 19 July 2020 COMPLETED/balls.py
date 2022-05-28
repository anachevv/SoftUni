import math

n_balls = int(input())
points = 0
red_balls = 0
orange_balls = 0
yellow_balls = 0
white_balls = 0
black_balls = 0
other_balls = 0
for ball_color in range(n_balls):
    current_color = input()

    if current_color == "red":
        points += 5
        red_balls += 1
    elif current_color == "orange":
        points += 10
        orange_balls += 1
    elif current_color == "yellow":
        points += 15
        yellow_balls += 1
    elif current_color == "white":
        points += 20
        white_balls += 1
    elif current_color == "black":
        points = math.floor(points / 2)
        black_balls += 1
    else:
        other_balls += 1

total_balls = red_balls + orange_balls + yellow_balls + white_balls + black_balls

print(f"Total points: {points}")
print(f"Red balls: {red_balls}")
print(f"Orange balls: {orange_balls}")
print(f"Yellow balls: {yellow_balls}")
print(f"White balls: {white_balls}")
print(f"Other colors picked: {other_balls}")
print(f"Divides from black balls: {black_balls}")
