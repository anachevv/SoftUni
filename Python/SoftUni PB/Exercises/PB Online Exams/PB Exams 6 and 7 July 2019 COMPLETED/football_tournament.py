team_name = input()
played_season_matches = int(input())
total_points = 0
won_games = 0
draw_games = 0
lost_games = 0
for x in range(played_season_matches):
    result = input()

    if result == "W":
        won_games += 1
        total_points += 3
    elif result == "D":
        draw_games += 1
        total_points += 1
    elif result == "L":
        lost_games += 1
        total_points += 0

if played_season_matches == 0:
    print(f"{team_name} hasn't played any games during this season.")
elif played_season_matches >= 1:
    win_rate = won_games / played_season_matches * 100
    print(f"{team_name} has won {total_points} points during this season.\nTotal stats:")
    print(f"## W: {won_games}")
    print(f"## D: {draw_games}")
    print(f"## L: {lost_games}")
    print(f"Win rate: {win_rate:.2f}%")
