first_team = ['A-' + str(x) for x in range(1, 11 + 1)]
second_team = ['B-' + str(x) for x in range(1, 11 + 1)]
game_is_terminated = False

sent_off_players = input().split()

for player in sent_off_players:
    if player in first_team:
        first_team.remove(player)
    elif player in second_team:
        second_team.remove(player)

    if (len(first_team) or len(second_team)) < 7:
        game_is_terminated = True
        break

print(f'Team A - {len(first_team)}; Team B - {len(second_team)}')

if game_is_terminated:
    print('Game was terminated')
