total_points = 0
winner = ""

while True:
    player_name = input()
    points = 0

    if player_name == "Stop":
        break

    for x in player_name:
        number = int(input())

        if number == ord(x):
            points += 10
        else:
            points += 2

        if total_points <= points:
            total_points = points
            winner = player_name

print(f"The winner is {winner} with {total_points} points!")
