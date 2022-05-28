import math

tournaments = int(input())
start_points = int(input())
points = 0
won_tournaments = 0

for x in range(tournaments):
    stage = input()

    if stage == "W":
        points += 2000
        won_tournaments += 1
    if stage == "F":
        points += 1200
    if stage == "SF":
        points += 720

points += start_points

print(f"Final points: {points}\nAverage points: {math.floor((points - start_points) / tournaments)}"
      f"\n{won_tournaments / tournaments * 100:.2f}%")
