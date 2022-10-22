command = input()
wins_counter = 0
losses_counter = 0

while command != "End of tournaments":

    if command == "End of tournaments":
        break

    tournament_name = command
    n = int(input())
    game_counter = 0
    teammates_points = 0
    enemy_points = 0
    difference = 0

    for x in range(n):
        teammates_points = int(input())
        enemy_points = int(input())
        game_counter += 1

        difference = abs(teammates_points - enemy_points)

        if teammates_points > enemy_points:
            wins_counter += 1
            print(f"Game {game_counter} of tournament {tournament_name}: win with {difference} points.")
        else:
            losses_counter += 1
            print(f"Game {game_counter} of tournament {tournament_name}: lost with {difference} points.")

    game_counter = 0

    command = input()

if command == "End of tournaments":
    print(f"{wins_counter / (wins_counter + losses_counter) * 100:.2f}% matches win")
    print(f"{losses_counter / (wins_counter + losses_counter) * 100:.2f}% matches lost")
