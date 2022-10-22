player_name = input()
player_points = 301
successful_shots_counter = 0
unsuccessful_shots_counter = 0
earned_points = 0

sector = input()

while sector != "Retire":
    earned_points = int(input())

    if sector == "Single":
        player_points -= earned_points
        if player_points < 0:
            player_points += earned_points
            unsuccessful_shots_counter += 1
        else:
            successful_shots_counter += 1
    elif sector == "Double":
        player_points -= earned_points * 2
        if player_points < 0:
            player_points += earned_points * 2
            unsuccessful_shots_counter += 1
        else:
            successful_shots_counter += 1
    elif sector == "Triple":
        player_points -= earned_points * 3
        if player_points < 0:
            player_points += earned_points * 3
            unsuccessful_shots_counter += 1
        else:
            successful_shots_counter += 1
    if player_points == 0:
        break

    sector = input()

if player_points == 0:
    print(f"{player_name} won the leg with {successful_shots_counter} shots.")
if sector == "Retire":
    print(f"{player_name} retired after {unsuccessful_shots_counter} unsuccessful shots.")
