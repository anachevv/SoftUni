import math

tournaments = int(input())
starting_points = int(input())
total_points = 0
won_tournaments = 0

for x in range(tournaments):
    stage = input()

    if stage == "W":
        total_points += 2000
        won_tournaments += 1
    elif stage == "F":
        total_points += 1200
    elif stage == "SF":
        total_points += 720

print(f"Final points: {total_points + starting_points}")
print(f"Average points: {math.floor(total_points / tournaments)}")
print(f"{won_tournaments / tournaments * 100:.2f}%")
